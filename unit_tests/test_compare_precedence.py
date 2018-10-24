import unittest
import sys
sys.path.insert(0,'..')
from shunting_yard import *


class TestComparePrecedence(unittest.TestCase):
    def test_for_empty_tokens(self):
        left = ""
        right = ""
        self.assertEqual(comparePrecedence(left, right), 0)

    def test_for_empty_left_token(self):
        left = ""
        right = "+"
        self.assertEqual(comparePrecedence(left, right), 1)

    def test_for_empty_right_token(self):
        left = "+"
        right = ""
        self.assertEqual(comparePrecedence(left, right), -1)
    
    def test_for_low_priority_tokens(self):
        left = "+"
        right = "+"
        self.assertEqual(comparePrecedence(left, right), 0)
    
    def test_for_left_high_token(self):
        left = "*"
        right = "+"
        self.assertEqual(comparePrecedence(left, right), 1)
    
    def test_for_right_high_token(self):
        left = "+"
        right = "/"
        self.assertEqual(comparePrecedence(left, right), -1)

    def test_for_special_character(self):
        left = "\*"
        right = "&"
        self.assertEqual(comparePrecedence(left, right), 0)