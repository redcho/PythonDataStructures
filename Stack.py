class Stack:
    def __init__(self):
        self.arr = []

    def is_empty(self):
        return self.arr == []

    def peek(self):
        return self.arr[len(self.arr)-1]

    def size(self):
        return len(self.arr)

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        return self.arr.pop()

    def __str__(self):
        return str(self.arr)