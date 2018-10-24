import unittest
import sys
sys.path.insert(0,'..')
from shunting_yard import *


class TestTokenize(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        tokens = tokenize(string)
        with self.assertRaises(StopIteration):
            next(tokens)
        
    def test_for_single_character_in_string(self):
        string = "F"
        for token in tokenize(string):
            self.assertEqual(token, "F")

    def test_for_multiple_character_in_string(self):
        string = "5 6 +"
        result = list(tokenize(string))
        self.assertListEqual(result, ["5", "6", "+"])

    def test_single_operator(self):
        tokens = list(tokenize('1+2'))
        self.assertListEqual(tokens, ['1', '+', '2'])

