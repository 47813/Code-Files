class DListNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DListType:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def addFront(self, data):
        node = DListNode(data, None, self.front)  # first node which means no data should be ahead the node and the
        # original front data should be the next data
        if self.size == 0:
            self.front = self.rear = node
        else:
            self.front.prev = node  # this would make a connection for any further addFront function
            self.front = node  # point the node as front
        self.size += 1

    def deleteFront(self):
        if not self.size == 0:
            data = self.front.data
            self.front = self.front.next  # move the front pointer to the next data
            if self.front is None:  # if there is no data when pointer is moved,
                self.rear = None  # it means there is no data meaning clear the list
            else:
                self.front.prev = None  # then, clear the front pointer's previous data, which is the data wanted to
                # be deleted
            self.size -= 1
            return data

    def addRear(self, data):
        node = DListNode(data, self.rear, None)  # last node which means no data should be behind the node and the
        # original rear data should be the previous data
        if self.size == 0:
            self.rear = self.front = node
        else:
            self.rear.next = node  # this would make a connection for any further addRear function
            self.rear = node  # point the node as rear
        self.size += 1

    def deleteRear(self):
        if not self.size == 0:
            data = self.rear.data
            self.rear = self.rear.prev  # move the rear pointer to second-latest data
            if self.rear is None:
                self.front = None  # if the moved pointer points at no data, clear the list
            else:
                self.rear.next = None  # remove the original rear data
            self.size -= 1
            return data

    def addPos(self, pos, data):
        if pos == 1:
            self.addFront(data)
        elif pos == self.size + 1:
            self.addRear(data)
        else:
            node = DListNode(data, None, None)
            p = self.front
            for i in range(1, pos - 1):
                p = p.next  # move the pointer to the given position's prev position

            node.prev = p  # since p is position's prev position, node's prev position should be p
            node.next = p.next  # since p is position's prev position, p.next should point at the next data, which
            # has to be pointed at node.next

            p.next.prev = node  # p.next's prev pointer should point at node
            p.next = node  # finally p's next data should be node
            self.size += 1

    def display(self):
        p = self.front
        while p is not None:
            print(p.data, end=" ")
            p = p.next
        print()


if __name__ == '__main__':
    dList = DListType()
    dList.addFront(4); dList.addFront(3); dList.display()
    dList.addFront(2); dList.addFront(1); dList.display()
    dList.addRear(5); dList.addRear(6); dList.display()
    dList.addRear(7); dList.addRear(8); dList.display()
    print(f"[{dList.deleteFront()}] deleted"); dList.display()
    print(f"[{dList.deleteRear()}] deleted"); dList.display()
    dList.addPos(3, "_3rd position_"); dList.display()
