import sys
from collections import deque


def bfs(sy, sx):
    queue = deque()
    visited[sy][sx] = 1
    cnt = 0
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        cnt += 1

        for i in range(4):
            dy, dx = y + DY[i], x + DX[i]

            if 0 <= dy < N and 0 <= dx < N:
                if ARR[dy][dx] and not visited[dy][dx]:
                    visited[dy][dx] = 1
                    queue.append((dy, dx))

    return cnt


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ARR = []
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(N):
        ARR.append(list(map(int, sys.stdin.readline().strip())))

    DY = [0, 1, 0, -1]
    DX = [1, 0, -1, 0]
    count = 0
    res = []
    for Y in range(N):
        for X in range(N):
            if ARR[Y][X] and not visited[Y][X]:
                res.append(bfs(Y, X))
                count += 1

    res.sort()

    print(count)
    for i in range(count):
        print(res[i])
