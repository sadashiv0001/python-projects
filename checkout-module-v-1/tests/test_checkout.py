import unittest
from checkoutKata.ShopCheckout import ShopCheckout

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        # sample CSV file for testing with the required pricing information=> it is required actually
        self.checkout = ShopCheckout('./items.csv')

    def test_empty_basket(self):
        expected_price = 0
        actual_price = self.checkout.calculate_total_price()
        self.assertEqual(actual_price, expected_price, f"Test Case 1: Failed. Expected {expected_price}, but got {actual_price}")

    def test_single_item(self):
        self.checkout.scan_item('A')
        expected_price = 50
        actual_price = self.checkout.calculate_total_price()
        self.assertEqual(actual_price, expected_price, f"Test Case 2: Failed. Expected {expected_price}, but got {actual_price}")

    def test_multiple_items(self):
        self.checkout.scan_item('A')
        self.checkout.scan_item('B')
        expected_price = 80
        actual_price = self.checkout.calculate_total_price()
        self.assertEqual(actual_price, expected_price, f"Test Case 3: Failed. Expected {expected_price}, but got {actual_price}")

    def test_various_items(self):
        test_cases = [
            ("CDBA", 115),
            ("AA", 100),
            ("AAA", 130),
            ("AAAA", 180),
            ("AAAAA", 230),
            ("AAAAAA", 260),
            ("AAAB", 160),  
            ("AAABB", 175),
            ("AAABBD", 190),
            ("DABABA", 190),
        ]

        for index, (basket, expected_price) in enumerate(test_cases, start=4):
            with self.subTest(basket=basket, expected_price=expected_price):
                self.checkout.reset_checkout()  # Reset the checkout happens here for each test case
                for item in basket:
                    self.checkout.scan_item(item)
                actual_price = self.checkout.calculate_total_price()
                self.assertEqual(actual_price, expected_price, f"Test Case {index}: Failed. Expected {expected_price}, but got {actual_price}")

if __name__ == '__main__':
    unittest.main()
