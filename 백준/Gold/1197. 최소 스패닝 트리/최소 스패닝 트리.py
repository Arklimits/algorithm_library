import sys
import heapq

read = sys.stdin.readline
V, E = map(int, read().split())
NODE = []
root = [i for i in range(V + 1)]

for i in range(E):
    a, b, c = map(int, read().split())
    heapq.heappush(NODE, (c, a, b))


def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]


def union(x, y):
    if find(x) != find(y):
        root[find(y)] = find(x)


check = 0
res = 0
while check < (V - 1):
    c, a, b = heapq.heappop(NODE)
    if find(a) != find(b):
        union(a, b)
        check += 1
        res += c
print(res)
