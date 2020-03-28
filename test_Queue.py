import unittest
import queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.empty_queue = queue.Queue()
        self.five_queue = queue.Queue()
        i = 0
        for x in range(5):
            self.five_queue.enqueue(i)
            i = i + 1

        self.five_start = queue.Queue()
        j = 5
        for x in range(5):
            self.five_start.enqueue(j)
            j = j - 1

    def test_length(self):
        self.assertEqual(self.empty_queue.length(), 0)
        self.empty_queue.enqueue(1)
        self.empty_queue.enqueue(2)
        self.empty_queue.enqueue(6)
        self.assertEqual(self.empty_queue.length(), 3)

    def test_first(self):
        self.assertEqual(self.five_queue.first(), 0)
        self.assertEqual(self.five_start.first(), 5)

    def test_last(self):
        self.assertEqual(self.five_queue.last(), 4)
        self.assertEqual(self.five_start.last(), 1)

    def test_enqueue(self):
        self.assertEqual(self.five_queue.length(), 5)
        self.assertEqual(self.five_queue.last(), 4)
        self.assertEqual(self.five_queue.first(), 0)
        self.five_queue.enqueue(9)
        self.assertEqual(self.five_queue.first(), 0)
        self.assertEqual(self.five_queue.last(), 9)
        self.assertEqual(self.five_queue.length(), 6)

    def test_dequeue(self):
        self.assertEqual(self.five_queue.length(), 5)
        self.assertEqual(self.five_queue.first(), 0)
        self.assertEqual(self.five_queue.last(), 4)
        self.five_queue.dequeue()
        self.assertEqual(self.five_queue.length(), 4)
        self.assertEqual(self.five_queue.first(), 1)
        self.assertEqual(self.five_queue.last(), 4)

    def test_empty(self):
        self.empty_queue.print()
        self.assertTrue(self.empty_queue.empty())
        self.empty_queue.enqueue(1)
        self.assertFalse(self.empty_queue.empty())
        self.empty_queue.dequeue()
        self.assertTrue(self.empty_queue.empty())
        self.assertEqual(self.empty_queue.dequeue(), None)
        self.assertEqual(self.empty_queue.first(), None)
        self.assertEqual(self.empty_queue.last(), None)


if __name__ == '__main__':
    unittest.main()
