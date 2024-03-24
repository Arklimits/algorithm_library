import sys
from heapq import heappush, heappop
from collections import deque

input = sys.stdin.readline


def program():
    arr = []
    for i in range(N):
        h, o = map(int, input().split())
        if h > o:
            arr.append((o, h))
        else:
            arr.append((h, o))

    d = int(input())

    queue = []

    for i in range(N):
        if arr[i][1] - arr[i][0] <= d:
            queue.append((arr[i][1], arr[i][0]))

    queue.sort()
    res = 0
    check = []
    for a, b in queue:
        heappush(check, b)

        while check:
            pivot = check[0]
            if a-pivot > d:
                heappop(check)
            else:
                break

        res = max(res, len(check))

    print(res)


# 선언부
N = int(input())

program()
