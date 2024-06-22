from ListNode import ListNode

class StackType:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        node = ListNode(data, self.top)  # insert the data at the latest data, which should be pointed by self.top
        self.top = node  # set the inserted node as self.top

    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.next  # move the pointer to the next data
            return data

    def peek(self):
        return self.top.data

    def display(self):
        if not self.isEmpty():
            p = self.top
            res = []
            while p is not None:
                res.append(p.data)
                p = p.next  # after putting the data into the list, move the pointer to the next value
            for i in res[::-1]:  # printing the data reversed, so it looks like a stack when popped
                print(i, end=" -> ")
            print("\b\b\b\n")
        else:
            print("Stack is empty")


if __name__ == "__main__":
    s = StackType()
    s.push('A')
    s.display()
    s.push('B')
    s.display()
    s.push('C')
    s.display()
    s.push('D')
    s.display()

    print(f"popped value: [{s.pop()}]")
    s.display()
    print(f"peeked value: [{s.peek()}]")
