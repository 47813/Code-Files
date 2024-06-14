from ListNode import ListNode


class LinearQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        node = ListNode(data, None)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node  # current latest element + 1
            self.rear = node  # move the pointer to the latest element

    def dequeue(self):
        if not self.isEmpty():
            res = self.front.data
            if self.rear == self.front:
                self.front = self.rear = None
            else:
                self.front = self.front.next
            return res
    def display(self):
        p = self.front
        while p is not None:
            print(f"[{p.data}] -> ", end='')
            p = p.next

        print("\b\b\b\n")


if __name__ == '__main__':
    q = LinearQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    q.dequeue()
    q.display()