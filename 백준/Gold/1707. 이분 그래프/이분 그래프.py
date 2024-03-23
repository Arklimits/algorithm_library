import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(pivot, color):
    global FLAG
    if VISIT[pivot] != -1:
        if VISIT[pivot] != color:
            FLAG = False
        return

    VISIT[pivot] = color
    color = (color+1) % 2

    for i in GRAPH[pivot]:
        dfs(i, color)

def program():  # 구동부
    for i in range(1, V+1):
        if VISIT[i] == -1:
            dfs(i, 1)

    if FLAG:
        print('YES')
    else:
        print('NO')


# 선언부
N = int(input())

for _ in range(N):
    V, E = map(int, input().split())
    GRAPH = [[] for _ in range(V + 1)]
    VISIT = [-2] + [-1 for _ in range(V)]
    FLAG = True

    for __ in range(E):
        F, T = map(int, input().split())
        GRAPH[F].append(T)
        GRAPH[T].append(F)

    for __ in range(N+1):
        GRAPH[__].sort()

    program()
