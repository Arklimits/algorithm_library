import sys
from heapq import heappush, heappop

def program():
    n = int(sys.stdin.readline())
    num = []
    for y in range(n):
        arr = list(map(int, sys.stdin.readline().split()))

        for x in range(n):
            if len(num) < n:
                heappush(num, arr[x])
            else:
                if arr[x] > num[0]:
                    heappop(num)
                    heappush(num, arr[x])

    print(num[0])


if __name__ == '__main__':
    program()
