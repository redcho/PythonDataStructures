class Queue:
    def __init__(self):
        self.arr = []

    def is_empty(self):
        return self.arr == []

    def enqueue(self, val):
        self.arr.insert(0, val)

    def size(self):
        return len(self.arr)

    def dequeue(self):
        return self.arr.pop()

    def __str__(self):
        return str(self.arr)