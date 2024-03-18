import sys

result = 2000000000

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

x.sort()

lp, rp = 0, n - 1

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

    if i + 1 <= check < n:
        if x[check] == -x[i]:
            print(x[i], x[check])
            exit()
        elif abs(x[i] + x[check]) < result:
            result = abs(x[i] + x[check])
            lp, rp = i, check

    if i + 1 <= check - 1 < n and abs(x[i] + x[check - 1]) < result:
        result = abs(x[i] + x[check - 1])
        lp, rp = i, check - 1

print(x[lp], x[rp])
