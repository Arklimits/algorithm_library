import sys

n = int(sys.stdin.readline())

arr = [0] * 10001

for i in range(n):
    a = int(sys.stdin.readline())
    arr[a] += 1

for i in range(len(arr)):
    if arr[i]:
        for j in range(arr[i]):
            print(i)
