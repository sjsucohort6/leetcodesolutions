# Deque() create a deque
# addFront(item)
# addRear(item)
# removeFront()
# removeRear()
# isEmpty()
# size()

class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # rear is the first index
    def addRear(self, item):
        self.items.insert(0, item)

    # front is the len(self.items) index
    def addFront(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()
d.addFront('hello')
d.addRear('world')
d.size()                                        # 2
print (d.removeFront() + ' ' + d.removeRear())    # 'hello world'
d.size()                                        # 0