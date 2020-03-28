import unittest
import stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.empty_stack = stack.Stack()
        self.five_stack = stack.Stack()

        i = 0
        for x in range(5):
            self.five_stack.push(i)
            i = i + 1

        self.five_start = stack.Stack()
        j = 5
        for x in range(5):
            self.five_start.push(j)
            j = j - 1

    def test_empty(self):
        self.empty_stack.print()
        self.assertTrue(self.empty_stack.empty())
        self.empty_stack.push(1)
        self.assertFalse(self.empty_stack.empty())
        self.empty_stack.pop()
        self.assertTrue(self.empty_stack.empty())
        self.assertEqual(self.empty_stack.pop(), None)

    def test_length(self):
        self.assertEqual(self.empty_stack.length(), 0)
        self.empty_stack.push(1)
        self.empty_stack.push(2)
        self.empty_stack.push(6)
        self.assertEqual(self.empty_stack.length(), 3)
        self.empty_stack.pop()
        self.assertEqual(self.empty_stack.length(), 2)

    def test_peek(self):
        self.assertEqual(self.five_start.peek(), 1)
        self.assertEqual(self.five_stack.peek(), 4)

    def test_push(self):
        self.assertEqual(self.empty_stack.length(), 0)
        self.empty_stack.push(2)
        self.assertEqual(self.empty_stack.length(), 1)
        self.assertEqual(self.empty_stack.peek(), 2)
        self.empty_stack.push(1)
        self.assertEqual(self.empty_stack.length(), 2)
        self.assertEqual(self.empty_stack.peek(), 1)

    def test_pop(self):
        self.assertEqual(self.five_stack.length(), 5)
        self.assertEqual(self.five_stack.peek(), 4)
        self.five_stack.pop()
        self.assertEqual(self.five_stack.length(), 4)
        self.assertEqual(self.five_stack.peek(), 3)
        self.five_stack.pop()
        self.five_stack.pop()
        self.assertEqual(self.five_stack.length(), 2)
        self.assertEqual(self.five_stack.peek(), 1)


if __name__ == '__main__':
    unittest.main()
