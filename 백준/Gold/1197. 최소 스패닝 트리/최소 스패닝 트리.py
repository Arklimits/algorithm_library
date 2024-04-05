import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 선언부
NODE = []
V, E = map(int, read().split())


# 구동부
def get_root(root, x):
    if root[x] != x:
        root[x] = get_root(root, root[x])
        return root[x]
    return x


def union(root, x, y):
    p1 = get_root(root, x)
    p2 = get_root(root, y)

    if p1 < p2:
        root[p2] = p1
    else:
        root[p1] = p2


def program():
    for _ in range(E):  # V를 E로 변경
        a, b, c = map(int, read().split())
        NODE.append((a, b, c))

    NODE.sort(key=lambda x: x[2])

    root = [i for i in range(V+1)]

    res = 0

    for a, b, c in NODE:
        if get_root(root, a) != get_root(root, b):
            union(root, a, b)
            res += c

    print(res)


program()
