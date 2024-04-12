import json
from dish import Dish


class Menu:
    def __init__(self, filename="D:/PPOIS/sem 4/lab1/savings/menu.json"):
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
