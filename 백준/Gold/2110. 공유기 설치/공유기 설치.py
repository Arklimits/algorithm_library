import sys


x = []
n, c = map(int, sys.stdin.readline().split())

for _ in range(n):
    x.append(int(sys.stdin.readline()))

x.sort()
start, end, dist = 1, x[-1] - x[0], 0


while start <= end:
    mid = (start + end) // 2

    router = 1
    house = x[0]
    for i in range(1, n):
        if x[i] - house >= mid:
            router += 1
            house = x[i]

    if router >= c:
        dist = max(dist, mid)
        start = mid + 1
    else:
        end = mid - 1


print(dist)
