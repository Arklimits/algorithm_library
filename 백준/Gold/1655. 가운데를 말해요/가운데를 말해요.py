import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def program():
    leftheap = []
    rightheap = []

    for i in range(N):
        num = int(input())

        if len(leftheap) == len(rightheap):
            heappush(leftheap, -num)
        else:
            heappush(rightheap, num)

        if rightheap and -leftheap[0] > rightheap[0]:
            temp = heappop(rightheap)
            heappush(rightheap, -heappop(leftheap))
            heappush(leftheap, -temp)

        print(-leftheap[0])


# 선언부
N = int(input())

program()
