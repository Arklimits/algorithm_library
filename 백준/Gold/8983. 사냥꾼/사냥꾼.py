import sys

limit = 1000000000
animal = []
shoot = []
count = 0

m, n, L = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
for _ in range(n):
    animal.append(list(map(int, sys.stdin.readline().split())))

x.sort()

for loc, dist in animal:
    if dist > L:
        continue
    elif dist == L:
        if loc in x:
            count += 1
    else:
        pivot = L - dist
        for i in range(pivot):
            if loc - i - 1 in x or loc + i + 1 in x:
                count += 1
                break

print(count)