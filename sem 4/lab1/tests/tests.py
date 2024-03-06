from waiter import Waiter, WaiterManager
from unittest.mock import patch, mock_open,  Mock
from dish import Dish
from restaurant import Restaurant
import unittest
from visitor import Visitor
from menu import Menu
from kitchen import Kitchen


class TestVisitor(unittest.TestCase):
    def test_make_an_order(self):
        menu_data = [{"name": "Dish1", "price": 10, "cooking_time": 15},
                     {"name": "Dish2", "price": 12, "cooking_time": 20}]
        menu_items = [Dish(item['name'], item['price'], item['cooking_time']) for item in menu_data]
        menu = Menu()
        menu.menu_items = menu_items

        visitor = Visitor("John")
        with patch("builtins.input", side_effect=["Dish1", "Dish2", "готово"]):
            visitor.make_an_order(menu)

        self.assertEqual(len(visitor.order), 2)
        self.assertEqual(visitor.bill, 22)

    def test_ask_for_a_bill(self):
        waiter_manager = WaiterManager()
        waiter = Waiter("Alice")
        waiter_manager.waiters = [waiter]

        visitor = Visitor("John")
        visitor.bill = 30
        visitor.order = [Dish("Dish1", 15, 20), Dish("Dish2", 10, 15)]

        with patch("builtins.input", return_value=5):
            with patch.object(Waiter, "take_order") as mock_take_order:
                visitor.ask_for_a_bill(waiter, waiter_manager)

        self.assertEqual(visitor.bill, 0)
        self.assertEqual(len(visitor.order), 0)
        mock_take_order.assert_called_once_with(visitor, 30, waiter_manager)

    def test_check_order(self):
        kitchen = Kitchen(chefs=[Mock()])
        visitor = Visitor("John")
        dish1 = Dish("Dish1", 15, 20)
        dish2 = Dish("Dish2", 10, 15)
        visitor.order = [dish1, dish2]

        with patch.object(Kitchen, "cook_dishes") as mock_cook_dishes:
            visitor.check_order(kitchen)

        mock_cook_dishes.assert_called_once_with([dish1, dish2])

    @patch("sys.exit")
    def test_leave_with_bill(self, mock_exit):
        visitor = Visitor("John")
        visitor.bill = 30
        with patch("builtins.print") as mock_print:
            visitor.leave()

        mock_print.assert_called_with("Сначала оплатите счет")
        mock_exit.assert_not_called()


class TestKitchen(unittest.TestCase):
    def test_cook_dishes(self):
        waiter = Waiter(name="John", salary=0)

        kitchen = Kitchen(chefs=[waiter])
        kitchen.max_progress_callback = Mock()

        dish1 = Mock(name="Dish1", cooking_time=30)
        dish2 = Mock(name="Dish2", cooking_time=40)

        dish1.waiter = waiter
        dish2.waiter = waiter

        kitchen.cook_dishes([dish1, dish2])

        expected_calls = [
            Mock(name="Dish1", percent=100),
            Mock(name="Dish2", percent=100)
        ]


class TestWaiter(unittest.TestCase):
    def test_take_order(self):
        waiter = Waiter(name="John", salary=0)
        waiter_manager = Mock()
        visitor = Visitor(name="Alice")

        with patch("builtins.input", side_effect=["10"]):
            waiter.take_order(visitor, 100, waiter_manager)

        self.assertEqual(waiter.salary, 30)

    def test_set_busy(self):
        waiter = Waiter(name="John", salary=0)
        self.assertFalse(waiter.is_busy())
        waiter.set_busy(True)
        self.assertTrue(waiter.is_busy())


class TestWaiterManager(unittest.TestCase):
    def test_hire_waiter(self):
        waiter_manager = WaiterManager(filename="test_waiters.json")
        waiter_manager.hire_waiter("Bob")

        self.assertIn("Bob", [waiter.name for waiter in waiter_manager.waiters])

    def test_assign_waiter(self):
        waiter_manager = WaiterManager(filename="test_waiters.json")
        waiter_manager.waiters = [Waiter(name="John")]

        visitor = Visitor(name="Alice")
        assigned_waiter = waiter_manager.assign_waiter(visitor)

        self.assertIsNotNone(assigned_waiter)
        self.assertTrue(assigned_waiter.is_busy())

        assigned_waiter = waiter_manager.assign_waiter(visitor)
        self.assertIsNone(assigned_waiter)


class TestMenu(unittest.TestCase):
    def test_load_menu_successful(self):
        mock_open_func = mock_open(read_data='[{"name": "Dish1", "price": 10, "cooking_time": 15}]')

        with patch('builtins.open', mock_open_func):
            menu = Menu(filename='test_menu.json')
            menu_items = menu.load_menu()

        self.assertEqual(len(menu_items), 1)
        self.assertIsInstance(menu_items[0], Dish)
        self.assertEqual(menu_items[0].name, 'Dish1')
        self.assertEqual(menu_items[0].price, 10)
        self.assertEqual(menu_items[0].cooking_time, 15)

    def test_load_menu_file_not_found(self):
        mock_open_func = mock_open()
        with patch('builtins.open', mock_open_func):
            mock_open_func.side_effect = FileNotFoundError

            menu = Menu(filename='nonexistent_menu.json')
            menu_items = menu.load_menu()

        self.assertEqual(len(menu_items), 0)

    def test_load_menu_invalid_json(self):
        mock_open_func = mock_open(read_data='invalid_json_data')

        with patch('builtins.open', mock_open_func):
            menu = Menu(filename='invalid_menu.json')
            menu_items = menu.load_menu()

        self.assertEqual(len(menu_items), 0)


class TestRestaurant(unittest.TestCase):
    def test_load_reviews_successful(self):
        mock_open_func = mock_open(read_data='[{"author": "John", "rating": 8, "comment": "Good food"}]')

        with patch('builtins.open', mock_open_func):
            restaurant = Restaurant(name='Test Restaurant')
            reviews = restaurant.load_reviews()

        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0]['author'], 'John')
        self.assertEqual(reviews[0]['rating'], 8)
        self.assertEqual(reviews[0]['comment'], 'Good food')

    def test_load_reviews_file_not_found(self):
        mock_open_func = mock_open()
        with patch('builtins.open', mock_open_func):
            mock_open_func.side_effect = FileNotFoundError

            restaurant = Restaurant(name='Nonexistent Restaurant')
            reviews = restaurant.load_reviews()

        self.assertEqual(len(reviews), 0)

    def test_load_reviews_invalid_json(self):
        mock_open_func = mock_open(read_data='invalid_json_data')

        with patch('builtins.open', mock_open_func):
            restaurant = Restaurant(name='Invalid Restaurant')
            reviews = restaurant.load_reviews()

        self.assertEqual(len(reviews), 0)


if __name__ == "__main__":
    unittest.main()
