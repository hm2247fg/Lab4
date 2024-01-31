import unittest 
from unittest import TestCase
from price_discount import discount  


class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_empty_list(self):  # tests for empty list
        prices = []
        self.assertIsNone(discount(prices))

    def test_duplicate_prices(self):  # test for duplicate prices
        prices = [10, 10, 10]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))

    # def test_calculation(self):  """Test accuracy of calculation of discounted price when given an original price and a discount rate"""
    #     prices = 100
    #     discount_rate = 0.2  # 20% discount
    #     expected_price = 80
    #     assert discount(prices, discount_rate) == expected_price

    # def test_discount_returns_original_when_rate_zero(self):  """Test if the function returns the original price when the discount rate is 0"""
    #     prices = [10, 4, 100]
    #     discount_rate = 0
    #     expected_price = 100
    #     assert discount(prices, discount_rate) == expected_price


if __name__ == '__main__':
    unittest.main()