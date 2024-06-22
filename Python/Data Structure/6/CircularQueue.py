from ListNode import ListNode


class CircularQueue:
    def __init__(self):
        self.tail = None  # points the last element of the list
        self.size = 0

    def isEmpty(self):
        return self.tail is None

    def enqueue(self, data):
        node = ListNode(data, None)  # declaring a new node. the next has to be None because it is not linked with
        # any other elements yet

        if self.isEmpty():
            node.next = node  # node's pointer should point itself because there is no elements except itself
            self.tail = node  # the last element is itself because again there are no elements except itself
        else:  # if the list is filled with 1 or more elements
            node.next = self.tail.next  # make the tail pointer point to the new node
            self.tail.next = node  # since the created node is the most recent node made, tail.next should point the
            # created node

        self.size += 1

    def dequeue(self):
        if not self.isEmpty():
            p = self.tail  # points at the end of the list
            q = p.next  # points at the end of the list's next pointer which is the firs element
            data = q.data  # first element's data

            if p == q:  # if there is only one element in the list
                self.tail = None  # reset the list
            else:
                p.next = q.next  # move each of the node by 1 so the last node would be deleted

            self.size -= 1
            return data
        else:
            print("No elements")

    def display(self):

        p = self.tail.next  # last element + 1 -> first element

        for i in range(self.size):
            print(f"[{p.data}] ->", end=' ')
            p = p.next

        print("\b\b\b   ")


if __name__ == '__main__':
    Q = CircularQueue()

    Q.enqueue('A')
    Q.display()
    Q.enqueue('C')
    Q.display()
    Q.enqueue('B')
    Q.display()
    print(f"deleted value: [{Q.dequeue()}]")
    Q.display()
    Q.enqueue('D')
    Q.display()
