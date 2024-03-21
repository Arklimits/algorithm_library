import sys


read = sys.stdin.readline


def press(depth, y, x):
    box = 0

    for i in range(y, y+depth):
        for j in range(x, x+depth):
            box += r[i][j]

    if box == depth**2:
        print(1, end='')
    elif box == 0:
        print(0, end='')
    else:
        print('(', end='')
        p = depth // 2
        press(p, y, x)
        press(p, y, x + p)
        press(p, y + p, x)
        press(p, y + p, x + p)
        print(')', end='')

    return


n = int(read())
x = []
r = [[0] * n for _ in range(n)]
for _ in range(n):
    x.append(read().strip())

for o in range(n):
    for q in range(n):
        r[o][q] = int(x[o][q])

press(n, 0, 0)