import sys


loads = sys.stdin.readlines

a, b, c = map(int, loads())
arr = [0] * 10
result = str(a*b*c)

for i in result:
    arr[int(i)] += 1

for i in range(10):
    print(arr[i])
