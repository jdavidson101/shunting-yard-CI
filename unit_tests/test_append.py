import unittest
import sys
sys.path.insert(0,'..')
from shunting_yard import *


class TestAppendToOuput(unittest.TestCase):
    def test_for_empty_string_and_token(self):
        string = ""
        token = ""
        self.assertEqual(appendToOutput(string, token), "")

    def test_for_empty_token(self):
        string = "4"
        token = ""
        self.assertEqual(appendToOutput(string, token), "4 ")

    def test_for_empty_string(self):
        string = ""
        token = "5"
        self.assertEqual(appendToOutput(string, token), token)

    def test_for_single_digits(self):
        string = "4"
        token = "5"
        self.assertEqual(appendToOutput(string, token), "4 5")

    def test_for_single_operator(self):
        string = "4 5"
        token = "+"
        self.assertEqual(appendToOutput(string, token), "4 5 +")