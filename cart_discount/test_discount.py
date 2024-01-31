import unittest 
from unittest import TestCase
from price_discount import discount  


class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    """if the result is none, test will pass"""
    def test_empty_list(self):  # defines test method for empty list
        prices = []  # initializes an empty list named prices
        self.assertIsNone(discount(prices))  # assertion - check if the result of calling discount with prices is none

    def test_duplicate_prices(self):  # defines test method for duplicate prices
        prices = [10, 10, 10]  # initializes a list named prices
        expected_discount = 10  # sets the expected discount value
        self.assertEqual(expected_discount, discount(prices))

    """Test accuracy of calculation of discounted price when given an original price and a discount rate"""
    def test_calculation(self):
        prices = 100
        discount_rate = 0.2  # 20% discount
        expected_price = 80
        assert discount(prices, discount_rate) == expected_price

    """Test if the function returns the original price when the discount rate is 0"""
    def test_discount_returns_original_when_rate_zero(self):
        prices = [10, 4, 100]
        discount_rate = 0
        expected_price = 100
        assert discount(prices, discount_rate) == expected_price


if __name__ == '__main__':
    unittest.main()