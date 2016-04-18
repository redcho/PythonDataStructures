from Node import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > val:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(val)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def search(self, val):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == val:
                found = True
            else:
                if current.get_data() > val:
                    stop = True
                else:
                    current = current.get_next()
        return found
