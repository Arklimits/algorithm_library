import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def program(start, dist):  # 구동부
    pivot = 1
    res = [300001] * (N+1)
    res[start] = 0
    queue = []
    heappush(queue, (0, start))

    while queue:
        cost, now = heappop(queue)

        if res[now] < cost:
            continue

        for i in road[now]:
            val = cost + 1
            if val < res[i]:
                res[i] = val
                heappush(queue, (val, i))

    for i in range(1, N+1):
        if res[i] == dist:
            print(i)
            pivot = 0

    if pivot:
        print(-1)


# 선언부
N, M, K, X = map(int, input().split())
road = [[] for _ in range(N + 1)]

for _ in range(M):
    __, ___ = map(int, input().split())
    road[__].append(___)

program(X, K)
