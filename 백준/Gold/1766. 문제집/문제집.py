import sys
from heapq import heappush, heappop


def program():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    in_degree = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        in_degree[b] += 1

    queue = []
    res = []
    for i in range(1, n + 1):
        if not in_degree[i]:
            heappush(queue, i)

    # print(in_degree)
    # print(graph)

    while queue:
        node = heappop(queue)
        res.append(node)
        for pivot in graph[node]:
            in_degree[pivot] -= 1
            if in_degree[pivot] == 0:
                heappush(queue, pivot)

    print(*res)


if __name__ == '__main__':
    program()
