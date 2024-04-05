import sys


def greedy():
    temp = 0
    count = 0
    
    for i in MEETING:
        if i[0] >= temp:
            temp = i[1]
            count += 1

    print(count)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    MEETING = []
    for _ in range(N):
        MEETING.append(list(map(int, sys.stdin.readline().split())))

    MEETING.sort(key=lambda x: (x[1], x[0]))

    greedy()
