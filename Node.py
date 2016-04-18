class Node:
    def __init__(self, init):
        self.data = init
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, val):
        self.data = val

    def set_next(self, node):
        self.next = node