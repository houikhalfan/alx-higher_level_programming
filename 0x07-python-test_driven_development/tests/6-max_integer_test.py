#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test case for an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        """Test case for a list of positive numbers"""
        numbers = [1, 2, 3, 4, 5]
        result = max_integer(numbers)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test case for a list of negative numbers"""
        numbers = [-1, -2, -3, -4, -5]
        result = max_integer(numbers)
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test case for a list of mixed positive and negative numbers"""
        numbers = [-5, 0, 10, -2, 7]
        result = max_integer(numbers)
        self.assertEqual(result, 10)

    def test_duplicate_numbers(self):
        """Test case for a list with duplicate numbers"""
        numbers = [3, 3, 3, 3, 3]
        result = max_integer(numbers)
        self.assertEqual(result, 3)

    def test_single_number(self):
        """Test case for a list with a single number"""
        numbers = [42]
        result = max_integer(numbers)
        self.assertEqual(result, 42)


if __name__ == '__main__':
    unittest.main()
