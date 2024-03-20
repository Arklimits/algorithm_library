import sys

m, n = map(int, sys.stdin.readline().split())
arr = [1] * (n + 1)
arr[0] = arr[1] = 0

for i in range(2, int(n**0.5) + 1):
    if arr[i]:
        for j in range(i+i, n+1, i):
            arr[j] = 0

for i in range(m, n+1):
    if arr[i]:
        print(i)
