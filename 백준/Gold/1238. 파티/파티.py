import sys
import heapq


def bfs(s):
    distance = [int(sys.maxsize)] * (n + 1)
    distance[s] = 0
    queue = []
    heapq.heappush(queue, (0, s))

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] >= dist:
            for pivot, cost in graph[node]:
                if dist + cost < distance[pivot]:
                    distance[pivot] = dist + cost
                    heapq.heappush(queue, (distance[pivot], pivot))

    return distance


if __name__ == '__main__':
    n, m, x = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))

    arr = bfs(x)
    arr[0] = 0
    for i in range(1, n+1):
        if i == x:
            continue
        arr[i] += bfs(i)[x]

    print(max(arr))
