import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def program():
    queue = []
    result = 0
    for i in range(N):
        heappush(queue, int(input()))

    while len(queue) > 1:
        # print(result, queue)
        temp = heappop(queue) + heappop(queue)
        heappush(queue, temp)
        result += temp

    print(result)


# 선언부
N = int(input())

program()
