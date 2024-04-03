import sys


def greedy(s):
    i, n = 0, 0
    while s - i > i:
        s -= i
        i += 1
        n += 1

    print(n)


if __name__ == '__main__':
    S = int(sys.stdin.readline())

    greedy(S)
