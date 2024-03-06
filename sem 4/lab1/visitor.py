from person import Person
from menu import Menu
from kitchen import Kitchen


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

    def ask_for_a_bill(self, waiter, waiter_manager):
        if self.bill != 0:
            print(f"Спасибо за посещение 'Вкусняшки Ганга'! Ваш счет составляет {self.bill} рублей.\n")
            waiter.take_order(self, self.bill, waiter_manager)
            self.bill = 0
            self.order = []
        else:
            print("Вы еще ничего не заказали в Ганге")

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
