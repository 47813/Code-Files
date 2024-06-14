class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:  # 조건
            self.size += 1  # 사이즈 추가
            for i in range(pos, self.size):
                self.array[i+1] = self.array[i]  # 한칸씩 뒤로 옮기기
            self.array[pos] = e  # pos 자리에 e 값 입력 하기

        else:
            pass

    def remove(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:  # 조건
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]  # index 가 pos 보다 큰 값들을 한칸씩 앞 당기기
            self.size -= 1  # size 감소
        else:
            pass

    def findItem(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return i

        return -1

    def __str__(self):
        return str(f"{self.array[0: self.size]} \n")


if __name__ == '__main__':
    array = ArrayList()
    array.insert(0, 1)
    array.insert(1, 2)
    array.insert(2, 3)
    array.insert(3, 4)

    print(array)