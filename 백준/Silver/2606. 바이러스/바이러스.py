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
    visit = dfs(1, [])
    print(len(visit)-1)


# 선언부
N = int(read())
M = int(read())

NODE = [[] for _ in range(N+1)]

for _ in range(M):
    loc, des = map(int, read().split())
    NODE[loc].append(des)
    NODE[des].append(loc)

for _ in range(1, N+1):
    NODE[_].sort()

program()
