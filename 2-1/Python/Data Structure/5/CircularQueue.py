class CircularQueue:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = e
        else:
            print("Overflow")

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.queue[self.front]
        else:
            print("Underflow")

    def peek(self):
        return self.queue[(self.front + 1 % self.capacity)]

    def display(self):
        print(f"Front: {self.front}, Rear : {self.rear}")
        i = self.front

        while i != self.rear:
            i = (i + 1) % self.capacity
            print(f"[{self.queue[i]}]", end='')
        print()

    def display2(self):
        print(self.queue[self.front + 1:self.rear + 1])


if __name__ == '__main__':
    Q = CircularQueue()
    Q.enqueue("A")
    Q.enqueue("B")
    Q.enqueue("C")
    Q.enqueue("D")
    Q.enqueue("E")
    Q.display()
