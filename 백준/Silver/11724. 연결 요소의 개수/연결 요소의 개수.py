import sys

sys.setrecursionlimit(10**6)
read = sys.stdin.readline

def dfs(pivot, visit):
    visit.append(pivot)
    for vertex in NODE[pivot]:
        if vertex not in visit:
            dfs(vertex, visit)
    return visit

def program():
    visit = []
    cnt = 0
    for i in range(1, N+1):
        if i not in visit:
            visit += dfs(i, [])
            cnt += 1

    print(cnt)


# 선언부
N, M = map(int, read().split())
NODE = [[] for _ in range(N+1)]

for _ in range(M):
    loc, des = map(int, read().split())
    NODE[loc].append(des)
    NODE[des].append(loc)

for _ in range(1, N+1):
    NODE[_].sort()

program()
