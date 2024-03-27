import sys
from collections import deque


def topo():
    queue = deque()
    time = 0

    for i in range(1, n+1):
        if not in_degree[i]:
            queue.append(i)
            total[i] = delay[i-1]

    while queue:
        pivot = queue.popleft()
        # print(f"{pivot=} {total=} {queue=}")

        for build in graph[pivot]:
            # print(f"{build=}")

            if total[build] < total[pivot] + delay[build-1]:
                total[build] = total[pivot] + delay[build-1]

            in_degree[build] -= 1
            if in_degree[build] <= 0:
                queue.append((build))

    return total[w]


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        delay = list(map(int, sys.stdin.readline().split()))
        graph = [[] for _ in range(n + 1)]
        in_degree = [0 for _ in range(n + 1)]
        total = [0 for _ in range(n+1)]

        for _ in range(k):
            x, y = map(int, sys.stdin.readline().split())
            graph[x].append(y)
            in_degree[y] += 1

        w = int(sys.stdin.readline())

        print(topo())
