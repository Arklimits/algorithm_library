import sys
from collections import deque


def bfs(queue, graph):
    while queue:
        pivot = queue.popleft()

        for i in range(4):
            ny = pivot[0] + DY[i]
            nx = pivot[1] + DX[i]

            if N > ny >= 0 and 0 <= nx < M:
                if not graph[ny][nx]:
                    graph[ny][nx] = graph[pivot[0]][pivot[1]] + 1
                    queue.append((ny, nx))

    res = 0
    for y in range(N):
        for x in range(M):
            if not graph[y][x]:
                print(-1)
                exit()
            else:
                res = max(res, graph[y][x])

    print(res-1)


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())
    QUEUE = deque()
    ARR = []

    for y in range(N):
        ARR.append(list(map(int, sys.stdin.readline().split())))
        for x in range(M):
            if ARR[y][x] == 1:
                QUEUE.append((y, x))

    DY = [0, 1, 0, -1]
    DX = [1, 0, -1, 0]

    bfs(QUEUE, ARR)
