class Dish:
    def __init__(self, name: str, price: int, cooking_time: int):
        self.name = name
        self.price = price
        self.cooking_time = cooking_time
        self.is_ready = False
