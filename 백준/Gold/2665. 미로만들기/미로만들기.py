import sys
from heapq import heappush, heappop

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def bfs(graph, y_s, x_s, y_e, x_e):
    res = [[2501] * N for _ in range(N)]
    queue = []
    heappush(queue, (0, (y_s, x_s)))

    res[y_s][x_s] = 0

    while queue:
        cost, (y, x) = heappop(queue)

        if res[y][x] < cost:
            continue

        for i in range(4):
            dy, dx = y+DY[i], x+DX[i]
            if 0 <= dy < N and 0 <= dx < N:
                val = cost + graph[dy][dx]
                if val < res[dy][dx]:
                    res[dy][dx] = val
                    heappush(queue, (val, (y+DY[i], x+DX[i])))

    print(res[y_e][x_e])


def program(arr):
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                arr[i][j] = 1
            else:
                arr[i][j] = 0


    bfs(arr, 0, 0, N-1, N-1)


# 선언부
N = int(input())
ARR = []
DY = [0, 1, 0, -1]
DX = [1, 0, -1, 0]

for _ in range(N):
    ARR.append(list(map(int, input().strip())))

program(ARR)
