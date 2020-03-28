class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#    def __repr__(self):
#        return 'Node <{}>'.format(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        # super().__init__()

    def length(self):
        if self.head is None:
            return 0
        curr = self.head
        size = 0
        while curr is not None:
            size = size + 1
            curr = curr.next
        return size

    def append(self, data):
        new_node = Node(data, None)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        return new_node

    def insert(self, index, data):
        # Adds element after specified index
        i = 1
        curr = self.head
        while i < index - 1 and curr is not None:
            curr = curr.next
            i = i + 1
        if curr is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node

    def delete(self, data_str):
        # Removes first item with specified value
        curr = self.head
        prev = None
        while curr and curr.data != data_str:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def remove(self, index):
        # Removes the element at the specified position
        curr = self.head
        prev = None
        x = 0

        while x < index:
            prev = curr
            curr = curr.next
            x += 1
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

        return curr

    def search(self, data_str):
        # Return first node that matches data_str
        if self.head is None:
            print("List has no elements")
            return
        curr = self.head
        while curr is not None:
            if curr.data == data_str:
                print(data_str + " found in list")
                return True
            curr = curr.next
        print(data_str + " not found in list")
        return False

    def is_empty(self):
        return self.head is None

    def print_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            curr = self.head
            while curr is not None:
                print(curr.data, " ")
                curr = curr.next


if __name__ == '__main__':
    print("Main in linked_list.py")