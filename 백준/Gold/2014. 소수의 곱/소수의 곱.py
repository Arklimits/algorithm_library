import sys
from heapq import heappush, heappop


def program():
    k, n = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    num = []

    for _ in range(k):
        heappush(num, arr[_])

    count = 0
    temp = 0
    
    while count < n:
        for i in range(k):
            temp = num[0]
            res = arr[i] * num[0]

            heappush(num, res)

            if temp % arr[i] == 0:
                break

        heappop(num)
        count += 1

    print(temp)


if __name__ == '__main__':
    program()
