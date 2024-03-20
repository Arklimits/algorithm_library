import sys


read = sys.stdin.readline
n = int(read())
arr = list(map(int, read().split()))
arr.sort()

def function():
    p1, p2, p3 = 0, n//2, n
    res = 3000000001

    for i in range(n):
        for k in reversed(range(i+1, n)):
            check = (i + k) // 2
            start, end = i+1, k-1

            while start <= end:
                mid = (start + end) // 2
                if arr[mid] >= -arr[i] + -arr[k]:
                    check = mid
                    end = mid - 1
                else:
                    start = mid + 1

            if i + 1 <= check <= k:
                if abs(arr[i] + arr[check] + arr[k]) < res:
                    res = abs(arr[i] + arr[check] + arr[k])
                    p1, p2, p3 = arr[i], arr[check], arr[k]

            if i + 1 <= check - 1 <= k:
                if abs(arr[i] + arr[check - 1] + arr[k]) < res:
                    res = abs(arr[i] + arr[check - 1] + arr[k])
                    p1, p2, p3 = arr[i], arr[check - 1], arr[k]

    return p1, p2, p3

print(*function())
