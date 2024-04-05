import sys


def dfs(now, visited):
    if visited == (1 << N) - 1:
        if MAP[now][0]:
            return MAP[now][0]
        else:
            return int(sys.maxsize)

    if (now, visited) in DP:
        return DP[(now, visited)]

    min_cost = sys.maxsize
    for dest in range(1, N):
        if MAP[now][dest] and not visited & (1 << dest):
            cost = dfs(dest, visited | (1 << dest)) + MAP[now][dest]
            min_cost = min(min_cost, cost)

    DP[(now, visited)] = min_cost

    return min_cost


if __name__ == '__main__':
    ans = int(1e10)
    N = int(sys.stdin.readline())
    MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    DP = {}

    print(dfs(0, 1))
