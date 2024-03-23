import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(pivot):
    if VISIT[pivot]:
        return
    VISIT[pivot] = 1
    for i in ARR[pivot]:
        if not VISIT[i]:
            PAR[i] = pivot
            dfs(i)

def program():  # 구동부
    dfs(1)

    for i in range(2, N+1):
        print(PAR[i])


# 선언부
N = int(input())
ARR = [[] for _ in range(N+1)]
PAR = [0 for _ in range(N+1)]
VISIT = [0 for _ in range(N+1)]

for _ in range(N-1):
    F, T = map(int, input().split())
    ARR[F].append(T)
    ARR[T].append(F)

for _ in range(N):
    ARR[_].sort()

program()
