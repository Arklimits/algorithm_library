import sys


def load():
    return sys.stdin.readline()


def level(start, end):
    while start <= end:
        diff = 0
        mid = (start + end) // 2

        for i in x:
            if i < mid:
                diff += mid - i
            else:
                break

        if diff <= k:
            start = mid + 1
        else:
            end = mid - 1

    print(end)


n, k = map(int, load().split())
x = [int(load()) for _ in range(n)]

x.sort()

level(x[0], x[-1] + k)