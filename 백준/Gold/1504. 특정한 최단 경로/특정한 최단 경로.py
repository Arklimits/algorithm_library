import sys
from heapq import heappush, heappop


def bfs(n, s, graph):
    visited = [False for _ in range(n + 1)]
    dijkstra = [sys.maxsize for _ in range(n + 1)]

    queue = [(0, s)]
    while queue:
        price, node = heappop(queue)

        if visited[node]:
            continue

        visited[node] = True
        dijkstra[node] = price

        for pivot, cost in graph[node]:
            if not visited[pivot]:
                heappush(queue, (price + cost, pivot))

    return dijkstra


def program():
    n, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, sys.stdin.readline().split())

    temp = bfs(n, 1, graph)
    res1, res2 = temp[v1], temp[v2]

    temp = bfs(n, v1, graph)
    res1 += temp[v2]
    res2 += temp[n]

    temp = bfs(n, v2, graph)
    res1 += temp[n]
    res2 += temp[v1]
    
    if res1 >= sys.maxsize or res2 >= sys.maxsize:
        print(-1)
    else:
        print(min(res1, res2))


if __name__ == '__main__':
    program()
