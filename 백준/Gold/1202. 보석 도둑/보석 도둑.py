import sys
from heapq import heappush, heappop
from collections import deque

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    arr = []
    bag = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    for _ in range(k):
        heappush(bag, int(sys.stdin.readline()))

    res = 0
    can = []
    arr.sort()
    arr = deque(arr)

    while bag:
        now = heappop(bag)

        while arr and arr[0][0] <= now:
            heappush(can, -arr.popleft()[1])
        if can:
            res += -heappop(can)

    print(res)
