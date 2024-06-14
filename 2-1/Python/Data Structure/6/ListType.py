class ListNode:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class ListType:
    def __init__(self) -> None:
        self.head = None

    def insertFirst(self, data):
        node = ListNode(data, self.head)
        self.head = node

    def deleteFirst(self):
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
            return data

    def getNode(self, pos):
        p = self.head
        for i in range(pos - 1):
            p = p.next
        return p

    def insert(self, pos, data):
        if pos == 1:
            self.insertFirst(data)
        else:
            prev = self.getNode(pos - 1)
            node = ListNode(data, prev.next)
            prev.next = node

    def delete(self, data):
        if self.head is None:
            return  # List is empty

        if self.head.data == data:
            self.deleteFirst()
            return

        scan = self.head
        while scan.next is not None:
            if scan.next.data == data:
                scan.next = scan.next.next
                return
            scan = scan.next

    def display(self):
        p = self.head
        while p is not None:
            if p.next is not None:
                print(p.data, end=" -> ")
            else:
                print(p.data)
            p = p.next

if __name__ == '__main__':
    L = ListType()
    L.insertFirst("A")
    L.insertFirst("B")
    L.display()
    L.insert(2, "C")
    L.insert(1, "D")
    L.display()
    L.insert(4, "E")
    L.insert(5, "E")
    L.display()
    L.deleteFirst()
    L.display()
    L.delete("C")
    L.display()
    L.delete("E")
    L.display()
    L.delete("A")
    L.display()
