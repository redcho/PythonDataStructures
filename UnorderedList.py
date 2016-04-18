from Node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, val):
        temp = Node(val)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        this = self.head
        count = 0
        while this != None:
            count += 1
            this = this.get_next()
        return count

    def search(self, val):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == val:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, val):
        previous = None
        current = self.head
        found = False
        while not found:
            if current.get_data() == val:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


