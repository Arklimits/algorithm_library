import sys
from collections import deque

read = sys.stdin.readline


def program():  # 구동부
    global K
    cnt, dir_pivot, full = 0, 0, 0
    x, y, dx, dy = 1, 1, 1, 0
    turn_index = 0

    SNAKE.append((1, 1))

    while 1:
        cnt += 1
        dy, dx = turn[turn_index]
        y, x = y+dy, x+dx

        if not 0 < x <= N or not 0 < y <= N or (y, x) in SNAKE:
            break

        for _ in range(K):
            temp = APPLE.popleft()
            if (y, x) == temp:
                K -= 1
                full = 1
                break
            else:
                APPLE.append(temp)

        SNAKE.append((y, x))
        if not full:
            SNAKE.popleft()

        full = 0

        if dir_pivot < L:
            if cnt >= int(ARROW[dir_pivot][0]):
                if ARROW[dir_pivot][1] == 'L':
                    turn_index -= 1
                    if turn_index < 0:
                        turn_index += 4
                else:
                    turn_index = (turn_index + 1) % 4
                dir_pivot += 1

    print(cnt)


# 선언부
N = int(read())
K = int(read())
APPLE = deque([tuple(map(int, read().split())) for _ in range(K)])
L = int(read())
ARROW = [tuple(read().split()) for _ in range(L)]
SNAKE = deque()

turn = [(0, 1), (1, 0), (0, -1), (-1, 0)]

program()
