import json
import random


class Waiter:
    def __init__(self, name: str, salary=0):
        self.name = name
        self.salary = salary
        self.busy = False

    def take_order(self, visitor, bill, waiter_manager):
        tip = 0
        if bill > 0:
            tip = float(input(f"Сколько вы хотите оставить чаевых официанту {self.name} (руб.)? "))
        total_salary = bill * 0.2 + tip
        self.salary += total_salary
        waiter_manager.save_waiters()
        print(f"Спасибо за заказ, {visitor.name}! Официант {self.name} получил {total_salary} руб.")

    def is_busy(self):
        return self.busy

    def set_busy(self, status: bool):
        self.busy = status


class WaiterManager:
    def __init__(self, filename="D:/BSUIR/4_semester/PPOIS/lab1/savings/waiters.json"):
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

    def assign_waiter(self, visitor):
        available_waiters = [waiter for waiter in self.waiters if not waiter.is_busy()]
        if available_waiters:
            waiter = random.choice(available_waiters)
            waiter.set_busy(True)
            print(f"Вас обслуживает официант {waiter.name}.")
            return waiter
        else:
            print("Извините, все официанты заняты. Подождите немного.")
            return None
