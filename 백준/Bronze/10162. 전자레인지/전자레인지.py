import sys


def greedy():
    global T

    a, b, c = 0, 0, 0
    if T >= 300:
        a = T // 300
        T %= 300
    if T >= 60:
        b = T // 60
        T %= 60
    if T >= 10:
        c = T // 10
        T %= 10

    if T > 0:
        print(-1)
        return

    print(a, b, c)


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    greedy()
