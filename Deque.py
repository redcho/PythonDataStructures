class Deque:
    def __init__(self):
        self.arr = []

    def add_rear(self, val):
        self.arr.insert(0, val)

    def add_front(self, val):
        self.arr.append(val)

    def size(self):
        return len(self.arr)

    def is_empty(self):
        return self.arr == []

    def remove_rear(self):
        return self.arr.pop(0)

    def remove_front(self):
        return self.arr.pop()

    def __str__(self):
        return str(self.arr)
