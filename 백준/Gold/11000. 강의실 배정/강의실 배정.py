import sys
from heapq import heappush, heappop
from collections import deque

def program():
    n = int(sys.stdin.readline())
    study = []

    for _ in range(n):
        s, e = map(int, sys.stdin.readline().split())
        study.append((s, e))

    study.sort()
    study = deque(study)
    heapq = []
    res = 0

    while study:
        now = study.popleft()

        if heapq:
            while heapq[0] <= now[0]:
                heappop(heapq)
                if not heapq:
                    break
        
        heappush(heapq, now[1])

        res = max(res, len(heapq))

    print(res)


if __name__ == '__main__':
    program()
