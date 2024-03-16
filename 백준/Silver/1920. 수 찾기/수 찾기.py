import sys


def divide(start, end, index):
    mid = (start + end) // 2

    if a[mid] == index:
        return 1
    elif end - start < 2:
        return 0
    elif a[mid] < index:
        return divide(mid, end, index)
    elif a[mid] > index:
        return divide(start, mid, index)
    return -1


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

for i in range(m):
    print(divide(0, n, b[i]))
