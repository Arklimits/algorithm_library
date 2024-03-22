import sys
from collections import deque

read = sys.stdin.readline

def dfs(pivot, visit):
    visit.append(pivot)
    for vertex in NODE[pivot]:
        if vertex not in visit:
            dfs(vertex, visit)
    return visit


def bfs(pivot):
    queue = deque([pivot])
    visit = [pivot]
    while queue:
        vertex = queue.popleft()
        for v in NODE[vertex]:
            if v not in visit:
                queue.append(v)
                visit.append(v)
    return visit


def program():
    dfs_visit = dfs(V, [])
    bfs_visit = bfs(V)

    print(' '.join(map(str, dfs_visit)))
    print(' '.join(map(str, bfs_visit)))


# 선언부
N, M, V = map(int, read().split())
NODE = [[] for _ in range(N+1)]

for _ in range(M):
    loc, des = map(int, read().split())
    if des not in NODE[loc]:
        NODE[loc].append(des)
    if loc not in NODE[des]:
        NODE[des].append(loc)

for _ in range(1, N+1):
    NODE[_].sort()

program()
