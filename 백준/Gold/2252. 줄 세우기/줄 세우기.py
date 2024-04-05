import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ARR = [[] for _ in range(N)]
CONNECTED = [0] * N

def topology(graph):
    queue = deque()
    res = deque()

    for i in range(N):
        if not CONNECTED[i]:
            queue.append(i)

    while queue:
        pivot = queue.popleft()
        res.append(pivot + 1)

        for i in graph[pivot]:
            if CONNECTED[i] > 1:
                CONNECTED[i] -= 1
            else:
                queue.append(i)

    for _ in range(N):
        print(res.popleft(), end=' ')

if __name__ == '__main__':
    for _ in range(M):
        __, ___ = map(int, input().split())
        ARR[__-1].append(___-1)
        CONNECTED[___ - 1] += 1

    topology(ARR)

