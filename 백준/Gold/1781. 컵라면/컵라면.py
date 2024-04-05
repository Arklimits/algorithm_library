import sys
from heapq import heappop, heappush


def greedy():
    queue = []

    for i in CUP:
        heappush(queue, i[1])
        if i[0] < len(queue):
            heappop(queue)

    print(sum(queue))


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    CUP = []
    for _ in range(N):
        t, c = map(int, sys.stdin.readline().split())
        CUP.append((t, c))

    CUP.sort()

    greedy()
