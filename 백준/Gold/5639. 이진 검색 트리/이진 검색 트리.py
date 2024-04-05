import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 구동부
def post(p1, p2):
    if p1 > p2:
        return

    mid = p2 + 1

    for i in range(p1 + 1, p2 + 1):
        if ARR[p1] < ARR[i]:
            mid = i
            break

    post(p1 + 1, mid - 1)
    post(mid, p2)

    print(ARR[p1])


def program():
    while True:
        try:
            ARR.append(int(read().rstrip()))
        except:
            break

    post(0, len(ARR) - 1)


# 선언부
ARR = []

program()
