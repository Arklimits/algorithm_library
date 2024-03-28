import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    res = 1001
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())

        if a <= b:
            res = min(res, b)

    if res < 1001:
        print(res)
    else:
        print(-1)
