import sys
from heapq import heappush, heappop


def dijkstra(s, n, graph):
    dist = [int(sys.maxsize) for _ in range(n+1)]
    dist[s] = 0
    queue = []

    heappush(queue, (0, s))

    while queue:
        price, node = heappop(queue)

        if price > dist[node]:
            continue

        for pivot, cost in graph[node]:
            if dist[pivot] > price + cost:
                dist[pivot] = price + cost
                heappush(queue, (dist[pivot], pivot))

    return dist


def program():
    v, e = map(int, sys.stdin.readline().split())
    start = int(sys.stdin.readline())
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))

    res = dijkstra(start, v, graph)

    for i in range(1, v+1):
        if res[i] < int(sys.maxsize):
            print(res[i])
        else:
            print('INF')


if __name__ == '__main__':
    program()
