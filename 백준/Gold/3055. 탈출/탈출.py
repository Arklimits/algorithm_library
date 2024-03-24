import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def bfs(graph):
    queue = []

    for y in range(R):
        for x in range(C):
            if graph[y][x] == '*':
                heappush(queue, (0, y, x, graph[y][x]))
            elif graph[y][x] == 'S':
                heappush(queue, (1, y, x, graph[y][x]))

    while queue:
        day, y, x, unit = heappop(queue)
        # print(f"{day=} {y=} {x=} {unit=}")
        # for i in range(R):
        #     print(graph[i])

        for i in range(4):
            dy, dx = y+DY[i], x+DX[i]
            if 0 <= dy < R and 0 <= dx < C:
                if graph[dy][dx] == '.':
                    graph[dy][dx] = unit
                    heappush(queue, (day+2, dy, dx, unit))

                elif graph[y][x] == 'S' and graph[dy][dx] == 'D':
                    print((day+1)//2)
                    break

                else:
                    continue
        else:
            continue
        break
    else:
        print("KAKTUS")

def program():
    arr = [list(input().strip()) for _ in range(R)]

    bfs(arr)


# 선언부
R, C = map(int, input().split())
DY = [0, 1, 0, -1]
DX = [1, 0, -1, 0]

program()
