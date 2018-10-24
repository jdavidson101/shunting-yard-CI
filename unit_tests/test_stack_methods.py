import unittest
import sys
sys.path.insert(0,'..')
from shunting_yard import *


class TestPeekAtStack(unittest.TestCase):
    # Program throws exception when stack is empty
    def test_for_empty_stack(self):
        stack = []
        with self.assertRaises(IndexError):
            peekAtStack(stack)

    def test_for_single_item_in_stack(self):
        stack = ["42"]
        self.assertEqual(peekAtStack(stack), "42")

    def test_for_multiple_items_in_stack(self):
        stack = ["42", "+"]
        self.assertEqual(peekAtStack(stack), "42")

class TestPopFromStack(unittest.TestCase):
    def test_for_empty_stack(self):
        stack = []
        with self.assertRaises(IndexError):
            peekAtStack(stack)

    def test_for_single_item_in_stack(self):
        stack = ["42"]
        self.assertEqual(peekAtStack(stack), stack[0])
        self.assertEqual(popFromStack(stack), "42")
        self.assertEqual(len(stack), 0)

    def test_for_multiple_items_in_stack(self):
        stack = ["+", "42"]
        self.assertEqual(peekAtStack(stack), "+")
        self.assertIsNotNone(popFromStack(stack))
        self.assertEqual(peekAtStack(stack), "42")

class TestPushToStack(unittest.TestCase):
    def test_for_empty_stack(self):
        stack = []
        token = "*"
        self.assertIsNone(pushToStack(stack, token))
        self.assertEqual(peekAtStack(stack), token)

    def test_for_single_item_in_stack(self):
        stack = ["*"]
        token = "7"
        self.assertEqual(peekAtStack(stack), stack[0])
        self.assertIsNone(pushToStack(stack, token))
        self.assertEqual(peekAtStack(stack), token)

    def test_for_multiple_items_in_stack(self):
        stack = ["*", "7"]
        token = "+"
        self.assertEqual(peekAtStack(stack), stack[0])
        self.assertIsNone(pushToStack(stack, token))
        self.assertEqual(peekAtStack(stack), token)

class TestStackIsEmpty(unittest.TestCase):
    def test_for_empty_stack(self):
        stack = []
        self.assertTrue(stackIsEmpty(stack))

    def test_for_single_item_in_stack(self):
        stack = ["7"]
        self.assertFalse(stackIsEmpty(stack))