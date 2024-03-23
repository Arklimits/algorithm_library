import sys

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(graph, y, x, visit) -> int:
    if visit[y][x]:
        return -1

    res = graph[y][x]
    visit[y][x] = 1

    for i in range(4):
        if graph[y+DY[i]][x+DX[i]] and not visit[y+DY[i]][x+DX[i]]:
            res += dfs(graph, y+DY[i], x+DX[i], visit)
    return res

def program():
    global ICE, FUT, YEAR

    while 1:
        YEAR += 1
        visit = [[0 for _ in range(M)] for _ in range(N)]

        for y in range(1, N-1):
            for x in range(1, M-1):
                cnt = 0
                for i in range(4):
                    if not ICE[y+DY[i]][x+DX[i]]:
                        cnt += 1

                FUT[y][x] = ICE[y][x] - cnt
                if FUT[y][x] < 0:
                    FUT[y][x] = 0

        # for y in range(N):
        #     print(ICE[y])

        total = 0
        for y in range(1, N-1):
            for x in range(1, M-1):
                ICE[y][x] = FUT[y][x]
                if ICE[y][x] > 0:
                    total += ICE[y][x]

        if not total:
            print(0)
            exit()

        y_s, x_s = 0, 0
        for y in range(1, N-1):
            for x in range(1, M-1):
                if ICE[y][x] > 0:
                    y_s, x_s = y, x
                    break
            if y_s or x_s:
                break

        if dfs(ICE, y_s, x_s, visit) < total:
            break

    print(YEAR)


# 선언부
N, M = map(int, input().split())
YEAR = 0
ICE = []
FUT = [[0 for _ in range(M)] for _ in range(N)]
DY = [0, 1, 0, -1]
DX = [1, 0, -1, 0]

for _ in range(N):
    ICE.append(list(map(int, input().split())))

program()
