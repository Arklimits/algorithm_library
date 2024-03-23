import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, pivot, visit):
    if visit[pivot]:
        return

    cnt = 1
    visit[pivot] = 1
    for i in graph[pivot]:
        if not visit[i]:
            cnt += dfs(graph, i, visit)
    return cnt
def program():
    res = 0

    for i in range(N):
        visit = [0 for _ in range(N)]
        if dfs(HEAVY, i, visit)-1 > N//2:
            res += 1

    for i in range(N):
        visit = [0 for _ in range(N)]
        if dfs(LIGHT, i, visit)-1 > N//2:
            res += 1

    print(res)


# 선언부
N, M = map(int, input().split())
HEAVY = [[] for _ in range(N)]
LIGHT = [[] for _ in range(N)]
for _ in range(M):
    H, L = map(int, input().split())
    HEAVY[L - 1].append(H - 1)
    LIGHT[H - 1].append(L - 1)

program()
