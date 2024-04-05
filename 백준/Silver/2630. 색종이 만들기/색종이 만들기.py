import sys


def paper(depth, y, x):
    global blue, white
    box = 0
    for i in range(y, y+depth):
        for j in range(x, x+depth):
            box += r[i][j]

    if box == depth**2:
        blue += 1
    elif box == 0:
        white += 1
    else:
        p = depth // 2
        paper(p, y, x)
        paper(p, y, x + p)
        paper(p, y + p, x)
        paper(p, y + p, x + p)
    return


n = int(sys.stdin.readline())
B = r = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
blue = white = 0

paper(n, 0, 0)

print(white)
print(blue)