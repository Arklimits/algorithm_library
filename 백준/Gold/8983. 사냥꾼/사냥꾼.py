import sys

count = 0

m, n, L = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
animal = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

x.sort()

for loc, dist in animal:
    start, end = 0, len(x) - 1
    left_shoot = loc + dist - L
    right_shoot = loc - (dist - L)

    if dist > L:
        continue
    elif dist == L:
        if loc in x:
            count += 1
        continue
    else:
        while start <= end:
            mid = (start + end) // 2

            if left_shoot <= x[mid] <= right_shoot:
                count += 1
                break
            elif left_shoot > x[mid]:
                start = mid + 1
            elif right_shoot < x[mid]:
                end = mid - 1

print(count)