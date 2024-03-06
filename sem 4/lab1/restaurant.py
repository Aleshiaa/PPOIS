import json


class Restaurant:
    def __init__(self, name: str):
        self.name = name
        self.reviews_file = "D:/BSUIR/4_semester/PPOIS/lab1/savings/reviews.json"
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
        print("Свободные столики: ")
        for tab in tables:
            if not tab.is_reserved:
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
