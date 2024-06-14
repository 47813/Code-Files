from ArrayList import ArrayList
array = ArrayList()

class ArraySet():
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def contains(self, e):
        for i in range(self.size):
            if e == self.array[i]:
                return True
        return False

    def insert(self, e):
        if not self.contains(e) and not self.isFull():  # 조건
            self.array[self.size] = e
            self.size += 1
        else:
            pass

    def delete(self, e):
        if not self.isEmpty() and self.contains(e):  # 조건
            for i in range(self.size):
                if e == self.array[i]:  # e 탐지
                    self.array[i] = self.array[i-1]  # e 삭제 및 size 까지의 e 들을 앞으로 한칸씩 앞 당기기
                    self.size -= 1  # size - 1
                return e

    def union(self, setB):
        setC = ArraySet()

        for i in range(self.size):
            setC.insert(self.array[i])  # 지금 까지의 array 를 하나의 set 에 저장

        for i in range(setB.size):
            setC.insert(setB.array[i])  # 새로운 set 의 e 들을 setC 로 insert (만약에 e 가 겹쳐도 insert 함수가 알아서 걸러 주기 때문에 상관 x)

        return setC

    def intersect(self, setB):
        intersectSet = ArraySet()  # 새로운 intersectSet set 를 생성

        for i in range(self.size):
            self.insert(self.array[i])  # 지금 까지의 집합을 하나의 set 에 저장

        for i in range(self.size):
            for j in range(setB.size):
                if self.array[i] == setB.array[j]:  # 만약에 2가지의 set 에 모두 e 가 들어 있다면
                    intersectSet.insert(self.array[i])  # intersectSet 에 저장

        return intersectSet

    def difference(self, setB):
        setDifference = ArraySet()  # 결과 ArraySet 생성

        for i in range(setB.size):
            if not self.contains(setB.array[i]):  # ArraySet 과 setB 가 겹치지 않을 때만 setDifference 에 삽입
                setDifference.insert(self.array[i])  # 이중 for 사용시 array 의 size 변동 으로 인해 for 고장

        return setDifference

    def __str__(self):
        return str(f"{self.array[0: self.size]} \n")


if __name__ == '__main__':
    S = ArraySet()
    S.insert(10)
    S.insert(20)
    S.insert(30)
    S.insert(40)

    S.delete(10)
    print(S)

    T = ArraySet()
    T.insert(10)
    T.insert(20)
    T.insert(40)
    T.insert(50)
    print(T)

    print(S.union(T))
    print(S.intersect(T))
    print(S.difference(T))