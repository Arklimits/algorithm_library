import sys
from collections import deque

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(graph, y, x, visit):
    stack = deque([(y, x)])

    while stack:
        py, px = stack.pop()
        if not visit[py][px]:
            visit[py][px] = 1

            cnt = 0

            for i in range(4):
                ny, nx = py+DY[i], px+DX[i]

                if not visit[ny][nx]:
                    if graph[ny][nx] <= 0:
                        cnt += 1
                    else:
                        stack.append((ny, nx))

            graph[py][px] -= cnt
            if graph[py][px] <= 0:
                ICE[(py, px)] = 0

    # for y in range(N):
    #     print(graph[y])
def program():
    global ICE, ARR, YEAR

    for y in range(1, N-1):
        for x in range(1, M-1):
            if ARR[y][x]:
                ICE[(y, x)] = 1

    while sum(ICE.values()) > 0:
        cnt = 1
        visit = [[0 for _ in range(M)] for _ in range(N)]

        for key, val in ICE.items():
            # print(f"{YEAR=}, {cnt=} {y=} {x=}")
            y, x = key
            if not visit[y][x] and val:
                if cnt > 1:
                    print(YEAR)
                    break
                dfs(ARR, y, x, visit)
                cnt += 1
        else:
            YEAR += 1
            continue
        break
    else:
        print(0)


# 선언부
N, M = map(int, input().split())
YEAR = 0
ARR = []
ICE = {}
DY = [0, 1, 0, -1]
DX = [1, 0, -1, 0]

for _ in range(N):
    ARR.append(list(map(int, input().split())))

program()
