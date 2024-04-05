import sys


def greedy(n, road, oil):
    cost = 0
    check = 0
    for i in range(n-1):
        if oil[check] >= oil[i+1]:
            cost += oil[check] * road[i]
            check = i+1
        else:
            cost += oil[check] * road[i]

    print(cost)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ROAD = list(map(int, sys.stdin.readline().split()))
    OIL = list(map(int, sys.stdin.readline().split()))

    greedy(N, ROAD, OIL)
