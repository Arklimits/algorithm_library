import sys
import heapq

input = sys.stdin.readline

N = int(input())
ARR = []
CONNECTED = [0 for _ in range(N)]

def topology(graph):
    queue = []
    new_number = N + 1
    res = [0 for _ in range(N)]

    for i in range(N):
        if not CONNECTED[i]:
            heapq.heappush(queue, -i)

    while queue:
        # print(queue)
        pivot = -heapq.heappop(queue)
        new_number -= 1
        res[pivot] = new_number

        for i in graph[pivot]:
            CONNECTED[i] -= 1
            if not CONNECTED[i]:
                heapq.heappush(queue, -i)

    if res.count(0) > 2:
        print(-1)
    else:
        print(*res)

if __name__ == '__main__':
    graph = [[] for _ in range(N)]

    for t in range(N):
        ARR = list(map(int, input().rstrip()))

        for idx, val in enumerate(ARR):
            if val == 1:
                graph[idx].append(t)
                CONNECTED[t] += 1

    topology(graph)
