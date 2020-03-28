import linked_list


class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        if self.stack.__len__() == 0:
            return True
        elif self.stack.__len__() > 0:
            return False

    def length(self):
        return self.stack.__len__()

    def push(self, data):
        self.stack.insert(0, data)

    def pop(self):
        if self.stack.__len__() == 0:
            return None
        else:
            return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def print(self):
        for x in self.stack:
            print(x)

