import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def program(start, end):  # 구동부
    res = [int(10e8)] * (N+1)
    res[start] = 0
    queue = []
    heappush(queue, (0, start))

    while queue:
        cost, now = heappop(queue)

        if res[now] < cost:
            continue

        for i in bus[now]:
            val = cost + i[1]

            if val < res[i[0]]:
                res[i[0]] = val
                heappush(queue, (val, i[0]))
                
    print(res[end])


# 선언부
N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]

for _ in range(M):
    __, ___, ____ = map(int, input().split())
    bus[__].append((___, ____))

S, E = map(int, input().split())


program(S, E)
