class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


M = 13


class HashTable:
    def __init__(self):
        self.table = [None] * M

    def hashFn(self, key):
        return key % M

    def insert(self, key):
        b = self.hashFn(key)
        node = Node(key)
        node.next = self.table[b]
        self.table[b] = node

    def display(self):
        for i in range(M):
            print(f"HT[{i}]: ", end="")
            n = self.table[i]
            if n is None:
                print("None")
            else:
                while n:
                    if n.next:
                        print(n.data, end=" -> ")
                    else:
                        print(n.data, end="")
                    n = n.next
                print()


# Example usage
ht = HashTable()
data = [45, 27, 88, 9, 71, 68, 46, 38, 24]
for key in data:
    ht.insert(key)

ht.display()

