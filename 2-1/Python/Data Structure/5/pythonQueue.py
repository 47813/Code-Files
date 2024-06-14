import queue

Q = queue.Queue()

for i in range(1, 10):
    Q.put(i)

print("큐의 내용: ", end="")

for j in range(1,10):
    print(Q.get(),end=" ")

print()

S = queue.LifoQueue(maxsize=20)

for k in range(1, 10):
    S.put(k)

for l in range(1, 10):
    print("스택의 내용: ", S.get(), end=" ")

