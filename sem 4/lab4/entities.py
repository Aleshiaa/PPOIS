import json
import random
import time
from concurrent.futures import ThreadPoolExecutor


class Person:
    def __init__(self, name: str):
        self.name = name

    def change_name(self, name: str):
        self.name = name


class Chef(Person):
    def __init__(self, name: str):
        super().__init__(name)


class Waiter:
    def __init__(self, name: str, salary=0):
        self.name = name
        self.salary = salary
        self.busy = False

    def take_order(self, visitor, bill, waiter_manager, tips: float):
        if tips == 0:
            tip = 0
            if bill > 0:
                tip = float(input(f"Сколько вы хотите оставить чаевых официанту {self.name} (руб.)? "))
            total_salary = bill * 0.2 + tip
            self.salary += total_salary
            waiter_manager.save_waiters()
            print(f"Спасибо за заказ, {visitor.name}! Официант {self.name} получил {total_salary} руб.")
        else:
            total_salary = bill * 0.2 + tips
            self.salary += total_salary
            waiter_manager.save_waiters()

    def is_busy(self):
        return self.busy

    def set_busy(self, status: bool):
        self.busy = status


class WaiterManager:
    def __init__(self, filename="D:/BSUIR/4_semester/PPOIS/lab4/savings/waiters.json"):
        self.filename = filename
        self.waiters = self.load_waiters()

    def load_waiters(self):
        try:
            with open(self.filename, "r") as file:
                waiters_data = json.load(file)
            return [Waiter(item['name'], item['salary']) for item in waiters_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_waiters(self):
        waiters_data = [{'name': waiter.name, 'salary': waiter.salary} for waiter in self.waiters]
        with open(self.filename, "w") as file:
            json.dump(waiters_data, file, indent=2)

    def hire_waiter(self, name: str):
        if name not in [waiter.name for waiter in self.waiters]:
            self.waiters.append(Waiter(name))
            self.save_waiters()
            print(f"Новый официант {name} нанят!")
        else:
            print("Официант с таким именем уже работает.")

    def assign_waiter(self):
        available_waiters = [waiter for waiter in self.waiters if not waiter.is_busy()]
        if available_waiters:
            waiter = random.choice(available_waiters)
            waiter.set_busy(True)
            print(f"Вас обслуживает официант {waiter.name}.")
            return waiter
        else:
            print("Извините, все официанты заняты. Подождите немного.")
            return None


class Table:
    def __init__(self, number: int):
        self.number = number
        self.is_reserved = False

    def reserve(self):
        self.is_reserved = True


class Restaurant:
    def __init__(self, name: str):
        self.name = name
        self.reviews_file = "D:/BSUIR/4_semester/PPOIS/lab4/savings/reviews.json"
        self.reviews = self.load_reviews()

    def load_reviews(self):
        try:
            with open(self.reviews_file, "r") as file:
                reviews = json.load(file)
            return reviews
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_reviews(self):
        with open(self.reviews_file, "w") as file:
            json.dump(self.reviews, file, indent=2)

    def add_reviews(self, author, rating, review):
        review_entry = {"author": author, "rating": rating, "comment": review}
        self.reviews.append(review_entry)
        self.save_reviews()

    def add_review(self, author: str):
        while True:
            rating = (input("Поставьте оценку от 1 до 10: "))
            if rating.isdigit():
                rating = int(rating)
                if 1 <= rating <= 10:
                    comment = input("Оставьте свой комментарий: ")
                    review = {"author": author, "rating": rating, "comment": comment}
                    self.reviews.append(review)
                    self.save_reviews()
                    print("Отзыв успешно добавлен!")
                    break
                else:
                    print("Оценка должна быть в пределе от 1 до 10, попробуйте еще раз")
            else:
                print("Введите оценку цифрой")

    def show_reviews(self):
        if not self.reviews:
            print("Пока нет отзывов.")
        else:
            print("Отзывы:")
            for review in self.reviews:
                print(f"{review['author']} оценил(а) ресторан на {review['rating']} баллов:")
                print(f"{review['comment']}\n")

    @staticmethod
    def reserve_a_table(tables, visitor):
        free_tables = [tab for tab in tables if not tab.is_reserved]

        if not free_tables:
            print("Извините, все столики заняты. Приходите позже.")
            return

        print("Свободные столики: ")
        for tab in free_tables:
            print(tab.number)

        while True:
            choice = input("Какой столик вы бы хотели забронировать?\n")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(tables):
                    if not tables[choice - 1].is_reserved:
                        tables[choice - 1].is_reserved = True
                        visitor.reservation = tables[choice - 1]
                        print(f"{visitor.name}, благодарим вас за бронирование {tables[choice - 1].number} столика")
                        break
                    else:
                        print(f"Извините, столик {choice} уже забронирован.")
                else:
                    print("Извините, такого столика нет.")
            else:
                print("Пожалуйста, введите номер столика цифрой.")


class Dish:
    def __init__(self, name: str, price: int, cooking_time: int):
        self.name = name
        self.price = price
        self.cooking_time = cooking_time
        self.is_ready = False


class Menu:
    def __init__(self, filename="D:/BSUIR/4_semester/PPOIS/lab4/savings/menu.json"):
        self.filename = filename
        self.menu_items = self.load_menu()

    def load_menu(self):
        try:
            with open(self.filename, "r") as file:
                menu_data = json.load(file)
            return [Dish(item['name'], item['price'], item['cooking_time']) for item in menu_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_menu(self):
        menu_data = [{'name': dish.name, 'price': dish.price, 'cooking_time': dish.cooking_time}
                     for dish in self.menu_items]
        with open(self.filename, "w") as file:
            json.dump(menu_data, file, indent=2)

    def add_dish(self, *dishes):
        for dish in dishes:
            if isinstance(dish, Dish):
                self.menu_items.append(dish)
            elif isinstance(dish, tuple) and len(dish) == 3:
                self.menu_items.append(Dish(*dish))
            else:
                print(f"Ошибка: Неверный формат блюда - {dish}")

        self.save_menu()

    def display_menu(self):
        print("Меню:")
        for item in self.menu_items:
            print(f"{item.name}: {item.price} руб.")

    def get_dish_by_name(self, name):
        for dish in self.menu_items:
            if dish.name == name:
                return dish
        return None


class Kitchen:
    def __init__(self, chefs):
        self.chefs = chefs

    def assign_chef(self, dish):
        return random.choice(self.chefs)

    def calculate_cook_time(self, order):
        cook_time = sum(dish.cooking_time for dish in order)
        return cook_time

    @staticmethod
    def cook_dish(dish, chef, max_progress_callback):
        dish_name = dish.name
        cooking_time = dish.cooking_time
        print(f"Шеф {chef.name} начал готовить блюдо: {dish_name}")
        for progress in range(0, 101, 10):
            time.sleep(cooking_time / 50)
            max_progress_callback(dish_name, progress)
        dish.is_ready = True
        print(f"\rБлюдо {dish_name} готово!")

    def cook_dishes(self, dishes):
        max_cooking_time = max(dish.cooking_time for dish in dishes)
        with ThreadPoolExecutor(max_workers=1) as executor:
            for dish in dishes:
                chef = self.assign_chef(dish)
                executor.submit(self.cook_dish, dish, chef, self.max_progress_callback)

    @staticmethod
    def max_progress_callback(dish_name: str, progress):
        if progress == 100:
            print(f"\rБлюдо {dish_name}: {progress}% готово", end='', flush=True)
        else:
            print(f"\rБлюдо {dish_name}: {progress}%", end='', flush=True)


class Visitor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.reservation = None
        self.order = []
        self.bill = 0

    def make_an_order(self, menu: Menu):
        while True:
            order_item = input("Скажите, что бы вы хотели попробовать в нашем чудесном ресторане? "
                               "(Введите 'готово', чтобы закончить заказ):\n")
            if order_item.lower() == 'готово':
                break
            found = False
            for item in menu.menu_items:
                if order_item == item.name:
                    self.order.append(item)
                    self.bill += item.price
                    found = True
                    print(f"Блюдо '{item.name}' добавлено в заказ.")
                    break
            if not found:
                print("Извините, такого блюда нет в меню.")

        if self.order:
            max_cooking_time = max(item.cooking_time for item in self.order)
            print(f"Время выполнения вашего заказа = {max_cooking_time} минут")
            print("Ваш заказ:")
            for order in self.order:
                print(order.name)

    def ask_for_a_bill(self, waiter, waiter_manager, tips, cli):
        if cli == "cli":
            if self.bill != 0:
                print(f"Спасибо за посещение 'Вкусняшки Ганга'! Ваш счет составляет {self.bill} рублей.\n")
                waiter.take_order(self, self.bill, waiter_manager, 0)
            else:
                print("Вы еще ничего не заказали в Ганге")
        else:
            if self.bill != 0:
                waiter.take_order(self, self.bill, waiter_manager, tips)
        self.bill = 0
        self.order = []

    def check_order(self, kitchen: Kitchen):
        if self.order:
            print("Ваш заказ:")
            for order in self.order:
                print(order.name)
            kitchen.cook_dishes(self.order)
        else:
            print("Вы еще ничего не заказали в нашем чудесном ресторане")

    def leave(self):
        if self.bill == 0:
            print("До встречи, приходите еще!")
            exit(1)
        else:
            print("Сначала оплатите счет")

    def add_to_order(self, dish: Dish):
        self.order.append(dish)
        self.bill += dish.price
