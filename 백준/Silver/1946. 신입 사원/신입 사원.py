import sys


def greedy():
    count = 1
    rank = 0
    for i in range(1, N):
        # print(f"{NEWBIE[0]=} {NEWBIE[i]=} {count=}")
        if NEWBIE[i][1] < NEWBIE[rank][1]:
            rank = i
            count += 1

    print(count)


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        NEWBIE = []

        N = int(sys.stdin.readline())
        for _ in range(N):
            NEWBIE.append(list(map(int, sys.stdin.readline().split())))

        NEWBIE.sort(key=lambda x: (x[0], x[1]))

        greedy()
