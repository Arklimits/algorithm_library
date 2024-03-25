import sys
from collections import deque
import heapq

input = sys.stdin.readline


def topology(s, e, forward, backward, distance):
    distance[s] = 0
    queue = []
    heapq.heappush(queue, (0, s))

    while queue:
        cost, node = heapq.heappop(queue)
        # print(f"{node=}, {cost=}, {queue=}, {distance=}")
        # print(f"{visited=}")
        if distance[node] < cost:
            continue
            
        for pivot, price in forward[node]:
            if distance[pivot] > cost + price:
                distance[pivot] = cost + price
                heapq.heappush(queue, (distance[pivot], pivot))

    print(-distance[e])

    cnt = 0
    visited = [False] * (N + 1)
    road = deque()
    visited[e] = True
    road.append(e)
    while road:
        node = road.popleft()

        for pivot, price in backward[node]:
            if distance[node] - price == distance[pivot]:
                cnt += 1
                if not visited[pivot]:
                    road.append(pivot)
                    visited[pivot] = True

    print(cnt)


if __name__ == '__main__':
    N = int(input())
    M = int(input())

    FORWARD = [[] for _ in range(N + 1)]
    BACKWARD = [[] for _ in range(N + 1)]
    DIST = [int(sys.maxsize)] * (N + 1)

    for _ in range(M):
        u, v, w = map(int, input().split())
        FORWARD[u].append((v, -w))
        BACKWARD[v].append((u, -w))

    S, E = map(int, input().split())

    topology(S, E, FORWARD, BACKWARD, DIST)
