import unittest
import sys
sys.path.insert(0,'..')
from shunting_yard import *


class TestIsDigit(unittest.TestCase):
    # Returns True for empty string
    def test_for_empty_string(self):
        token = ""
        self.assertFalse(isDigit(token))
    
    def test_for_integer_parameter(self):
        token = "1"
        self.assertTrue(isDigit(token))
        with self.assertRaises(TypeError):
            isDigit(1)

    def test_for_token(self):
        token = "+"
        self.assertFalse(isDigit(token))

    # Can accept more than single character and return true if numbers are in sequence
    def test_for_multiple_digits_in_sequence(self):
        token = "123"
        self.assertFalse(isDigit(token))

    def test_for_multiple_digits_out_of_sequence(self):
        token = "213"
        self.assertFalse(isDigit(token))

class TestIsANumber(unittest.TestCase):
    # Returns true for empty string
    def test_for_empty_string(self):
        token = ""
        self.assertFalse(isNumber(token))

    def test_for_character(self):
        token = "a"
        self.assertFalse(isNumber(token))
    
    def test_for_single_digit(self):
        token = "7"
        self.assertTrue(isNumber(token))
        with self.assertRaises(TypeError):
            isNumber(7)

    def test_for_multiple_digits(self):
        token = "6291"
        self.assertTrue(isNumber(token))
        with self.assertRaises(TypeError):
            isNumber(6291)
    
    def test_for_mixed_integers_characters(self):
        token = "4e"
        self.assertFalse(isNumber(token))

class TestIsLeftBracket(unittest.TestCase):
    # Returns True for empty string
    def test_for_empty_string(self):
        token = ""
        self.assertFalse(isLeftBracket(token))

    def test_for_right_bracket(self):
        token = ")"
        token2 = "]"
        self.assertFalse(isLeftBracket(token))
        self.assertFalse(isLeftBracket(token2))

    def test_for_left_bracket(self):
        token = "("
        token2 = "["
        self.assertTrue(isLeftBracket(token))
        self.assertTrue(isLeftBracket(token2))

    def test_for_integer(self):
        token = "2"
        self.assertFalse(isLeftBracket(token))
        with self.assertRaises(TypeError):
            isLeftBracket(2)

    def test_for_character(self):
        token = "a"
        self.assertFalse(isLeftBracket(token))

class TestIsRightBracket(unittest.TestCase):
    # Returns True for empty string
    def test_for_empty_string(self):
        token = ""
        self.assertFalse(isRightBracket(token))

    def test_for_right_bracket(self):
        token = ")"
        token2 = "]"
        self.assertTrue(isRightBracket(token))
        self.assertTrue(isRightBracket(token2))

    def test_for_left_bracket(self):
        token = "("
        token2 = "["
        self.assertFalse(isRightBracket(token))
        self.assertFalse(isRightBracket(token2))

    def test_for_integer(self):
        token = "2"
        self.assertFalse(isRightBracket(token))
        with self.assertRaises(TypeError):
            isLeftBracket(2)

    def test_for_character(self):
        token = "a"
        self.assertFalse(isRightBracket(token))  