import sys

result = 2000000000

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

x.sort()

small, big = 0, n - 1

for i in range(n):
    check = n
    start, end = i + 1, n - 1

    while start <= end:
        mid = (start + end) // 2
        if x[mid] >= -x[i]:
            check = mid
            end = mid - 1
        else:
            start = mid + 1

    if i + 1 <= check - 1 < n and abs(x[i] + x[check - 1]) < result:
        result = abs(x[i] + x[check - 1])
        small, big = i, check - 1

    if i + 1 <= check < n and abs(x[i] + x[check]) < result:
        result = abs(x[i] + x[check])
        small, big = i, check

print(x[small], x[big])
