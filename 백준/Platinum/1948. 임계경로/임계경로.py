import sys
from collections import deque

input = sys.stdin.readline


def topology(s, e, forward, backward, connected, distance):
    distance[s] = 0
    queue = deque()
    queue.append(s)

    while queue:
        node = queue.popleft()
        # print(f"{node=}, {cost=}, {queue=}, {distance=}")
        # print(f"{visited=}")
        for pivot, cost in forward[node]:
            connected[pivot] -= 1

            if distance[pivot] > distance[node] + cost:
                distance[pivot] = distance[node] + cost
            if connected[pivot] == 0:
                queue.append(pivot)

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
    CONNECT = [0] * (N + 1)
    DIST = [0] * (N + 1)

    for _ in range(M):
        u, v, w = map(int, input().split())
        FORWARD[u].append((v, -w))
        BACKWARD[v].append((u, -w))
        CONNECT[v] += 1

    S, E = map(int, input().split())

    topology(S, E, FORWARD, BACKWARD, CONNECT, DIST)
