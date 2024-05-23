from entities import *
from server import WebServer
from flask import render_template, request, redirect, session, url_for
import json


class CLIController:

    def __init__(self):
        pass

    @staticmethod
    def perform(tables, gang: Restaurant, menu: Menu, waiter_manager: WaiterManager,
                chefs, kitchen: Kitchen):

        switch_dict = {
            1: lambda: gang.reserve_a_table(tables, visitor),
            2: lambda: menu.display_menu(),
            3: lambda: visitor.make_an_order(menu),
            4: lambda: visitor.ask_for_a_bill(available_waiter, waiter_manager, 0, "cli"),
            5: lambda: visitor.leave(),
            6: lambda: visitor.check_order(kitchen),
            7: lambda: gang.add_review(visitor.name),
            8: gang.show_reviews
        }

        print("Добро пожаловать в ресторан 'Вкусняшки Ганга'")
        visitor = Visitor(" ")
        visitor.change_name(input("Как вас зовут?\n"))
        available_waiter = waiter_manager.assign_waiter()
        print(f"{visitor.name}, что вы хотели бы сделать?")

        while True:
            print("1. 🪑 Забронировать столик\n"
                  "2. 🍜 Посмотреть меню\n"
                  "3. 📋 Сделать заказ\n"
                  "4. 💷 Попросить счет\n"
                  "5. 🚪 Уйти\n"
                  "6. 📓 Подождать заказ\n"
                  "7. 📝 Оставить отзыв\n"
                  "8. 📖 Прочитать отзывы\n")

            try:
                user_choice = int(input("Введите: "))
                switch_dict.get(user_choice, lambda: print("Неверный вариант."))()
            except ValueError:
                print("Пожалуйста, введите число.")


class WebController:
    def __init__(self, webserver: WebServer, tables, gang: Restaurant, menu: Menu, waiter_manager: WaiterManager,
                 chefs, kitchen: Kitchen):
        self.visitor = Visitor(" ")
        self.webserver = webserver
        self.tables = tables
        self.gang = gang
        self.menu = menu
        self.waiter_manager = waiter_manager
        self.chefs = chefs
        self.kitchen = kitchen
        self.available_waiter = self.waiter_manager.assign_waiter()
        self.webserver.add_route(route="/", handler_func=self.hello_restaurant, methods=["GET"])
        self.webserver.add_route(route="/submit_name", handler_func=self.submit_name, methods=["POST"])
        self.webserver.add_route(route="/main", handler_func=self.main_page, methods=["GET"])
        self.webserver.add_route(route="/view_menu", handler_func=self.view_menu, methods=["GET"])
        self.webserver.add_route(route="/book_table", handler_func=self.book_table, methods=["GET", "POST"])
        self.webserver.add_route(route="/place_order", handler_func=self.place_order, methods=["GET", "POST"])
        self.webserver.add_route(route="/ask_for_a_bill", handler_func=self.ask_for_a_bill, methods=["GET", "POST"])
        self.webserver.add_route(route="/wait_order", handler_func=self.wait_order, methods=["GET"])
        self.webserver.add_route(route="/leave_review", handler_func=self.leave_review, methods=["GET", "POST"])
        self.webserver.add_route(route="/read_reviews", handler_func=self.read_reviews, methods=["GET"])
        self.webserver.add_route(route="/leave", handler_func=self.leave, methods=["GET"])

    def perform(self):
        self.webserver.run()

    @staticmethod
    def hello_restaurant():
        return render_template("hello.html")

    @staticmethod
    def submit_name():
        username = request.form.get('username')
        if username:
            session['username'] = username
            return redirect(url_for('main_page'))
        return redirect(url_for('hello_restaurant'))

    def main_page(self):
        username = session.get('username')
        if username:
            self.visitor.change_name(username)
            if self.available_waiter is not None:
                return render_template("main.html", username=username, available_waiter=self.available_waiter.name)
            else:
                return render_template("main.html", username=username, available_waiter="Закончились")

        return redirect(url_for('hello_restaurant'))

    @staticmethod
    def view_menu():
        with open('savings/menu.json', 'r', encoding='utf-8') as f:
            menu_data = json.load(f)
        return render_template('view_menu.html', dishes=menu_data)

    def book_table(self):
        if request.method == "POST":
            table_number = int(request.form.get("table_number"))
            for table in self.tables:
                if table.number == table_number and not table.is_reserved:
                    table.reserve()
                    break
            return redirect(url_for('main_page'))

        free_tables = [table for table in self.tables if not table.is_reserved]
        if len(free_tables) > 0:
            return render_template('book_table.html', tables=free_tables)
        else:
            return render_template('error.html', error="Извините, нет свободных столиков!")

    def place_order(self):
        if request.method == "POST":
            selected_dishes = request.form.getlist('dishes')
            if selected_dishes:
                for dish_name in selected_dishes:
                    dish = self.menu.get_dish_by_name(dish_name)
                    if dish:
                        self.visitor.add_to_order(dish)
            return redirect(url_for('main_page'))

        with open('savings/menu.json', 'r', encoding='utf-8') as f:
            menu_data = json.load(f)
        return render_template('place_order.html', dishes=menu_data)

    def ask_for_a_bill(self):
        if request.method == "POST":
            tips = float(request.form.get('tips'))
            if tips:
                self.visitor.ask_for_a_bill(self.available_waiter, self.waiter_manager, tips, "web")

            return redirect(url_for('main_page'))
        if self.visitor.bill != 0:
            return render_template('ask_for_a_bill.html', waiter=self.available_waiter.name,
                                   price=self.visitor.bill)
        else:
            return render_template('error.html', error="Вы еще ничего не заказали!")

    def wait_order(self):
        chef = self.kitchen.assign_chef(self.visitor.order)
        cook_time = self.kitchen.calculate_cook_time(self.visitor.order)
        if self.visitor.bill != 0:
            return render_template('wait_order.html', chef_name=chef.name, cook_time=cook_time)
        else:
            return render_template('error.html', error="Вы еще ничего не заказали!")

    def leave_review(self):
        if request.method == "POST":
            rating = request.form.get('rating')
            review = request.form.get('review')
            if rating and review:
                self.gang.add_reviews(self.visitor.name, rating, review)
                return redirect(url_for('main_page'))
        return render_template('leave_review.html')

    @staticmethod
    def read_reviews():
        with open('savings/reviews.json', 'r', encoding='utf-8') as f:
            review_data = json.load(f)
        return render_template('read_reviews.html', reviews=review_data)

    def leave(self):
        if self.visitor.bill == 0:
            return render_template('leave.html')
        else:
            return render_template('error.html', error="Сначала оплатите заказ!")
