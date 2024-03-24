import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
M = int(input())
ARR = [[] for _ in range(N)]
CONN = [0 for _ in range(N)]
CALC = [[0 for _ in range(N)] for _ in range(N)]

def topology(graph):
    queue = deque()

    for i in range(N):
        if not CONN[i]:
            queue.append(i)

    while queue:
        pivot = queue.popleft()

        for i, cost in graph[pivot]:
            # print(f"{pivot=} {i=} {cost=}")
            if not sum(CALC[pivot]):
                # print(f"{i=} {pivot=} {CALC[i][pivot]=} {cost=}")
                CALC[i][pivot] += cost
            else:
                for j in range(N):
                    # print(f"{pivot=} {i=} {j=} {CALC[i][j]=} {CALC[pivot][j]=} {cost=}")
                    CALC[i][j] += CALC[pivot][j] * cost

            CONN[i] -= 1
            if CONN[i] <= 0:
                queue.append(i)

    for i in range(N):
        if CALC[N-1][i] > 0:
            print(i+1, CALC[N-1][i])

        # for i in range(N):
        #     print(CALC[i])


if __name__ == '__main__':
    for _ in range(M):
        x, y, z = map(int, input().split())
        ARR[y-1].append((x-1, z))
        CONN[x - 1] += 1

    topology(ARR)
