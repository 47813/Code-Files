from CircularQueue import CircularQueue

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '0', '1', '0', '0', 'x'],
    ['1', '1', '1', '1', '1', '1'],
]

size = 6


def isValidPos(r, c):
    if 0 <= r < size and 0 <= c < size:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True

    return False

def BFS():
    Q = CircularQueue(50)
    Q.enqueue((1,0))
    print("BFS : ")

    while not Q.isEmpty():
        pos = Q.dequeue()
        print(pos, end=" -> ")
        (r, c) = pos

        if (map[r][c] == "x"):
            return True
        else:
            map[r][c] = '.'  # 지나간 곳이면 점을 찍어 표시
            if isValidPos(r - 1, c): Q.enqueue((r - 1, c))  # 상
            if isValidPos(r + 1, c): Q.enqueue((r + 1, c))  # 하
            if isValidPos(r, c - 1): Q.enqueue((r, c - 1))  # 좌
            if isValidPos(r, c + 1): Q.enqueue((r, c + 1))  # 우

            Q.display2()
    return False


if __name__ == "__main__":
    result = BFS()
    if (result == True):
        print("Success")

    else: print("False")
