import sys


def union(root, x, y):
    root[x] = y


def find(root, x):
    if root[x] != x:
        root[x] = find(root, root[x])
        return root[x]
    return x


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    graph = []

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph.append((a, b, c))

    graph.sort(key=lambda x: x[2])

    root = [i for i in range(n + 1)]
    count = 0
    res = 0

    for a, b, c in graph:
        root_a = find(root, a)
        root_b = find(root, b)

        if root_a != root_b:
            union(root, root_a, root_b)
            res += c
            count += 1

    print(res)
