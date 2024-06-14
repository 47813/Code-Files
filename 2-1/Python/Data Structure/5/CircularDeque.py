from CircularQueue import CircularQueue


class CircularDeque(CircularQueue):  # inheritance (CircularQueue)
    def __init__(self):
        super().__init__()  # recall inheritance function

    def addRear(self, e):
        self.enqueue(e)

    def deleteFront(self):
        self.dequeue()

    def getFront(self):
        self.peek()

    def addFront(self, e):
        if not self.isFull():
            self.queue[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            pass

    def deleteRear(self):
        if not self.isEmpty():
            e = self.queue[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return e
        else:
            pass

    def getRear(self):
        return self.queue[self.rear]


if __name__ == "__main__":

    import random
    DQ = CircularDeque()

    for i in range(4):
        DQ.addFront(random.randint(65, 90))
    DQ.display()

    for i in range(4):
        DQ.addRear(random.randint(65, 90))
    DQ.display()

    for i in range(2):
        DQ.deleteFront()

    for i in range(2):
        DQ.deleteRear()

    DQ.display()