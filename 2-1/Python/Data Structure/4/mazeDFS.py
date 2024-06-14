from ArrayStack import ArrayStack

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1'],
]

size = 6


def isValidPos(r, c):  # 갈 수 있는 길인지 판단
    if 0 <= r < size and 0 <= c < size:
        if map[r][c] == '0' or map[r][c] == 'x':  # 길이 0 이거나 x 일때만 가능 (지나온 길은 . 으로 표현 하기에 상관 x)
            return True

    return False


def DFS():
    print("DFS : ")
    S = ArrayStack(100)  # DFS 계산을 위한 새로운 ArrayStack 생성
    S.push((1, 0))  # 출발 지점의 좌표인 (1,0) 을 삽입

    while not S.isEmpty():  # ArrayStack 이 모두 출력 될 때 까지 (즉, x까지 도달 할 때 까지)
        pos = S.pop()
        print(pos, end=" -> ")  # 가장 마지막 에 들어 온 값을 먼저 출력
        (r, c) = pos

        if map[r][c] == "x":
            return True  # 지나갈 수 있는 길
        else:
            map[r][c] = '.'  # 지나간 곳이면 점을 찍어 표시 (표시를 하지 않으면 지나온 길을 다시 탐색 하기 때문)
            if isValidPos(r - 1, c):
                S.push((r - 1, c))  # 상
            if isValidPos(r + 1, c):
                S.push((r + 1, c))  # 하
            if isValidPos(r, c - 1):
                S.push((r, c - 1))  # 좌
            if isValidPos(r, c + 1):
                S.push((r, c + 1))  # 우

            S.display()
    return False


if __name__ == "__main__":
    result = DFS()
    if result:
        print("Success")

    else:
        print("False")
