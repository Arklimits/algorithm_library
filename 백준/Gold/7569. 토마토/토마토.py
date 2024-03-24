import sys
from collections import deque

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def bfs(graph):
    queue = deque()
    res = 0

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if graph[z][y][x] == 1:
                    queue.append((z, y, x, 1))

    while queue:
        z, y, x, cost = queue.popleft()

        for i in range(6):
            dz, dy, dx = z+DZ[i], y+DY[i], x+DX[i]
            if 0 <= dz < H and 0 <= dy < N and 0 <= dx < M:
                if not graph[dz][dy][dx]:
                    graph[dz][dy][dx] = cost + 1
                    queue.append((dz, dy, dx, cost + 1))

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if not graph[z][y][x]:
                    print(-1)
                    exit()
                res = max(res, graph[z][y][x])

    print(res-1)

def program(arr):
    arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    visit = [[[0] * M for _ in range(N)] for _ in range(H)]
    visit[0][0][0] = 1

    bfs(arr)


# 선언부
M, N, H = map(int, input().split())
ARR = []
DZ = [0, 0, 0, 0, 1, -1]
DY = [0, 1, 0, -1, 0, 0]
DX = [1, 0, -1, 0, 0, 0]

program(ARR)
