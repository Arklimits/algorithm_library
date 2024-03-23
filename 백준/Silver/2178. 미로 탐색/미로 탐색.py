import sys
from collections import deque

read = sys.stdin.readline


def program(start):  # 구동부
    y_e, x_e = N-1, M-1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    queue = deque()
    queue.append(start)

    while len(queue):
        y, x = queue.popleft()
        if (y, x) == (y_e, x_e):
            break

        for i in range(4):

            if 0 <= y + dy[i] <= y_e and 0 <= x + dx[i] <= x_e:
                if arr[y+dy[i]][x+dx[i]] == 1:
                    queue.append((y+dy[i], x+dx[i]))
                    arr[y+dy[i]][x+dx[i]] = arr[y][x] + 1

    print(arr[y_e][x_e])


# 선언부
N, M = map(int, read().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, read().strip())))

program((0, 0))
