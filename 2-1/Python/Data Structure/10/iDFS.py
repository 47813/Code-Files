Vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AdjVer = [[1, 2],
          [0, 3],
          [0, 3, 4],
          [1, 2, 5],
          [2, 6, 7],
          [3],
          [4, 7],
          [4, 6]]

from queue import LifoQueue

visited = [False] * len(Vertex)

def iDFS(u):
    S = LifoQueue()
    S.put(u)

    while not S.empty():
        u = S.get()

        if not visited[u]:
            visited[u] = True
            print(Vertex[u], end=" ")

        flag = True
        for v in AdjVer[u]:
            if not visited[v]:
                if flag:
                    S.put(u)
                    flag = False
                S.put(v)


if __name__ == '__main__':
    print("iDFS(A) : ", end="")
    iDFS(0)
