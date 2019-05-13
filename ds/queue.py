# Queue() to create a queue
# enqueue(item) to add to the rear
# dequeue() removes from the front
# isEmpty() is the bool
# size() returns the size

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item) # insert for FIFO

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.size()        # 0
q.enqueue(1)
q.enqueue(2)
q.dequeue()     # 1