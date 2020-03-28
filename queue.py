
class Queue:
    def __init__(self):
        self.queue = []

    def length(self):
        return self.queue.__len__()

    def enqueue(self, data):
        self.queue.append(data)
        pass

    def dequeue(self):
        if self.queue.__len__() == 0:
            return None
        else:
            return self.queue.pop(0)

    def first(self):
        if self.queue.__len__() == 0:
            return None
        else:
            return self.queue[0]

    def last(self):
        if self.queue.__len__() == 0:
            return None
        else:
            return self.queue[self.length() - 1]

    def empty(self):
        if self.queue.__len__() == 0:
            return True
        elif self.queue.__len__() > 0:
            return False

    def print(self):
        for x in self.queue:
            print(x)
