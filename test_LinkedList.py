import unittest
import linked_list
import json


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.node1 = linked_list.Node('1')
        self.node2 = linked_list.Node('2')
        self.node3 = linked_list.Node('3')
        self.test_list = linked_list.LinkedList()

    def convert_to_string(self, new_list):
        tmp_str = ""
        if new_list.head is None:
            print("List has no element")
            return
        else:
            curr = new_list.head
            while curr is not None:
                tmp_str = tmp_str + curr.data
                curr = curr.next
        return tmp_str

    def test_list_node(self):
        self.assertEqual(self.test_list.head, None)

    def test_length(self):
        self.assertEqual(self.test_list.length(), 0)
        self.test_list.append('second')
        self.assertEqual(self.test_list.length(), 1)
        self.test_list.append('third')
        self.assertEqual(self.test_list.length(), 2)
        self.test_list.remove(1)
        self.assertEqual(self.test_list.length(), 1)

    def test_is_empty(self):
        self.assertTrue(self.test_list.is_empty())
        self.test_list.append(self.node1)
        self.assertFalse(self.test_list.is_empty())
    
    def test_append(self):
        self.test_list = linked_list.LinkedList()
        self.test_list.head = linked_list.Node("A")
        node2 = linked_list.Node("B")
        node3 = linked_list.Node("C")
        self.test_list.head.next = node2
        node2.next = node3

        lower_list = linked_list.LinkedList()
        lower_list.append("a")
        lower_list.append("b")
        lower_list.append("c")

        upper_string = self.convert_to_string(self.test_list)
        lower_string = self.convert_to_string(lower_list)
        to_upper_string = lower_string.upper()
        to_lower_string = upper_string.lower()

        self.assertEqual(upper_string, to_upper_string)
        self.assertEqual(lower_string, to_lower_string)

    def test_insert(self):
        self.test_list = linked_list.LinkedList()
        self.test_list.head = linked_list.Node("A")
        insert_node = linked_list.Node("1")
        node2 = linked_list.Node("B")
        node3 = linked_list.Node("C")
        self.test_list.head.next = insert_node
        insert_node.next = node2
        node2.next = node3

        lower_list = linked_list.LinkedList()
        lower_list.append("a")
        lower_list.append("b")
        lower_list.append("c")
        lower_list.insert(1, "1")

        upper_string = self.convert_to_string(self.test_list)
        lower_string = self.convert_to_string(lower_list)
        to_upper_string = lower_string.upper()
        to_lower_string = upper_string.lower()

        self.assertEqual(upper_string, to_upper_string)
        self.assertEqual(lower_string, to_lower_string)

    def test_delete(self):
        self.test_list = linked_list.LinkedList()
        self.test_list.head = linked_list.Node("A")
        node3 = linked_list.Node("C")
        self.test_list.head.next = node3

        lower_list = linked_list.LinkedList()
        lower_list.append("a")
        lower_list.append("b")
        lower_list.append("c")
        lower_list.delete("b")

        upper_string = self.convert_to_string(self.test_list)
        lower_string = self.convert_to_string(lower_list)
        to_upper_string = lower_string.upper()
        to_lower_string = upper_string.lower()

        self.assertEqual(upper_string, to_upper_string)
        self.assertEqual(lower_string, to_lower_string)

    def test_remove(self):
        self.test_list = linked_list.LinkedList()
        self.test_list.head = linked_list.Node("A")
        node3 = linked_list.Node("C")
        self.test_list.head.next = node3

        lower_list = linked_list.LinkedList()
        lower_list.append("a")
        lower_list.append("b")
        lower_list.append("c")
        lower_list.remove(1)

        upper_string = self.convert_to_string(self.test_list)
        lower_string = self.convert_to_string(lower_list)
        to_upper_string = lower_string.upper()
        to_lower_string = upper_string.lower()

        self.assertEqual(upper_string, to_upper_string)
        self.assertEqual(lower_string, to_lower_string)

    def test_search(self):
        self.test_list = linked_list.LinkedList()
        self.test_list.append("a")
        self.test_list.append("b")
        self.test_list.append("c")

        self.assertTrue(self.test_list.search("b"))
        self.assertFalse(self.test_list.search("d"))
        self.test_list.delete("b")
        self.assertFalse(self.test_list.search("b"))


if __name__ == '__main__':
    unittest.main()
