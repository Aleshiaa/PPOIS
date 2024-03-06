from menu import Menu
from visitor import Visitor
from restaurant import Restaurant
from table import Table
from waiter import WaiterManager
from chef import Chef
from kitchen import Kitchen


tables = [Table(1), Table(2), Table(3), Table(4), Table(5)]
gang = Restaurant('Ганг')
menu = Menu()
waiter_manager = WaiterManager()
chefs = [Chef("Рахмат"), Chef("Сора"), Chef("Митахши")]
kitchen = Kitchen(chefs)

switch_dict = {
    1: lambda: gang.reserve_a_table(tables, visitor),
    2: lambda: menu.display_menu(),
    3: lambda: visitor.make_an_order(menu),
    4: lambda: visitor.ask_for_a_bill(available_waiter, waiter_manager),
    5: lambda: visitor.leave(),
    6: lambda: visitor.check_order(kitchen),
    7: lambda: gang.add_review(visitor.name),
    8: gang.show_reviews
}

print("Добро пожаловать в ресторан 'Вкусняшки Ганга'")
visitor = Visitor(input("Как вас зовут?\n"))
available_waiter = waiter_manager.assign_waiter(visitor)
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
