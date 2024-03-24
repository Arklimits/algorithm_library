import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph):
    queue = deque()
    check = [0 for _ in range(K+1)]
    pivot = 1

    res = sys.maxsize
    queue.append((K, 0))

    while queue:
        price, count = queue.popleft()

        for i in range(len(graph)):
            val = price - graph[i]
            # print(f"{price=} - {graph[i]=} = {val}")
            if val > 0 and count < res:
                if not check[val]:
                    queue.append((val, count + 1))
                    check[val] = 1
            elif val == 0:
                res = min(res, count+1)
                pivot = 0
            else:
                break

    if pivot:
        print(-1)
    else:
        print(res)

def program(arr):

    for i in range(len(arr)):
        if arr[i] > K:
            arr[i] = 0

    arr = list(set(arr))
    arr.sort()

    bfs(arr)


# 선언부
N, K = map(int, input().split())
ARR = []
for _ in range(N):
    ARR.append(int(input()))
program(ARR)
