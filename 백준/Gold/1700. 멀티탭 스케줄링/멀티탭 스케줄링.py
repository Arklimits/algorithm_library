import sys


def greedy():
    queue = set()
    count = 0

    for i in range(K):
        now = ORDER.pop(0)

        # print(now, queue, count)

        if len(queue) < N:
            queue.add(now)
            continue

        if now in queue:
            continue

        longest, nextj = -1, -1
        for plugged in queue:
            if plugged not in ORDER:
                nextj = plugged
                break
            else:
                nextplugged = ORDER.index(plugged)
                if longest < nextplugged:
                    longest = nextplugged
                    nextj = plugged

        if nextj == -1:
            exit(-1)
        queue.discard(nextj)
        queue.add(now)
        count += 1

    print(count)


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    ORDER = list(map(int, sys.stdin.readline().split()))

    greedy()
