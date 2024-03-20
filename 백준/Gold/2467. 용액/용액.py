import sys


read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))


def function():
    lp, rp = 0, n
    res = 2000000000

    for i in range(n):
        check = n
        start, end = i+1, n-1

        while start <= end:
            mid = (start + end) // 2
            if arr[mid] >= -arr[i]:
                check = mid
                end = mid - 1
            else:
                start = mid + 1

        if i + 1 <= check < n:
            if abs(arr[i] + arr[check]) < res:
                res = abs(arr[i] + arr[check])
                lp, rp = arr[i], arr[check]

        if i + 1 <= check - 1 < n:
            if abs(arr[i] + arr[check - 1]) < res:
                res = abs(arr[i] + arr[check - 1])
                lp, rp = arr[i], arr[check - 1]

    return lp, rp


print(*function())
