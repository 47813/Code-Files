class ArrayStack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity-1

    def push(self, e):
        if not self.isFull():  # 조건
            self.top += 1  # top + 1
            self.array[self.top] = e  # e 를 index 가장 위 (top) 에 저장
        else:
            print("Stack Overflow")

    def pop(self):
        if not self.isEmpty():  # 조건
            self.top -= 1  # top - 1
            return self.array[self.top+1]  # 삭제 되기 전의 값을 출력
        else:
            print("Stack Underflow")

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("Stack Underflow")

    def sortedPush(self, e):
        if self.isEmpty() or e > self.peek:
            self.push(e)
        else:
            temp = self.pop()
            self.sortedPush(e)
            self.push(temp)
    def __str__(self):
        return (str(self.array[0:self.top+1]))

    def display(self):
        print(self.array[self.top::-1])


if __name__ == '__main__':
    s = ArrayStack(10)

    data = [5,3,8,1,2,7]
    for d in data:
        s.sortedPush(d)
    print(s)
