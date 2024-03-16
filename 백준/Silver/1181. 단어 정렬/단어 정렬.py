import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    c = sys.stdin.readline().rstrip()
    if c not in arr:
        arr.append(c)

arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)
