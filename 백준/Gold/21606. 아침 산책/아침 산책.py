import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, pivot, visit):
    global CNT

    # print(f"NOW IN: {pivot=}")
    if start != pivot:
        if PLACE[pivot]:
            CNT += 1
            return

    visit[pivot] = 1

    for i in GRAPH[pivot]:
        if not visit[i]:
            dfs(start, i, visit)

def program():  # 구동부
    pivot = 0

    if sum(PLACE) < 2:
        print(0)
    elif sum(PLACE) == 2:
        print(2)
    else:
        for _ in range(N - 1):
            F, T = map(int, input().split())
            GRAPH[F - 1].append(T - 1)
            GRAPH[T - 1].append(F - 1)

        for i in range(N):
            if len(GRAPH[i]) > 2:
                pivot = 1
                break

        if pivot:
            for i in range(N):
                visit = [0 for _ in range(N)]
                if PLACE[i]:
                    # print(f"START {i=}")
                    dfs(i, i, visit)

            print(CNT)
            
        else:
            print(2*(sum(PLACE)-1))


# 선언부
N = int(input())
CNT = 0
GRAPH = [[] for _ in range(N)]
PLACE = list(map(int, input().strip()))

program()