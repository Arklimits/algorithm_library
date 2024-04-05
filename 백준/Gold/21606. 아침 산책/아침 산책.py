import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(pivot, visit):
    global CNT
    visit[pivot] = 1
    count = 0

    for i in GRAPH[pivot]:
        # print(f"{i=} {PLACE[i]=} {visit[i]=}")
        if PLACE[i]:
            count += 1
        elif not visit[i] and not PLACE[i]:
            count += dfs(i, visit)
    return count

def program():  # 구동부
    if sum(PLACE) < 2:
        print(0)
    elif sum(PLACE) == 2:
        print(2)
    else:
        global CNT
        visit = [0 for _ in range(N)]
        pivot = 0

        for _ in range(N - 1):
            f, t = map(int, input().split())
            GRAPH[f - 1].append(t - 1)
            GRAPH[t - 1].append(f - 1)

            if PLACE[f-1] and PLACE[t-1]:
                CNT += 2

        for i in range(N):
            if len(GRAPH[i]) > 2:
                pivot = 1
                break

        if pivot:
            for i in range(N):
                if not PLACE[i] and not visit[i]:
                    res = dfs(i, visit)
                    CNT += res * (res-1)
            print(CNT)

        else:
            print(2*(sum(PLACE)-1))


# 선언부
N = int(input())
CNT = 0
GRAPH = [[] for _ in range(N)]
PLACE = list(map(int, input().strip()))

program()