import time
import random
from concurrent.futures import ThreadPoolExecutor


class Kitchen:
    def __init__(self, chefs):
        self.chefs = chefs

    def assign_chef(self, dish):
        return random.choice(self.chefs)

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
