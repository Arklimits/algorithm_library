import sys

read = sys.stdin.readline


def program(jump):
    for i in range(n):
        removed.append(str(queue.pop(jump)))
        jump += k - 1

        if not len(queue):
            break

        if jump >= len(queue):
            jump %= len(queue)


n, k = map(int, read().split())
queue = []
removed = []
for _ in range(n):
    queue.append(_+1)

program(k-1)

print('<' + ', '.join(removed) + '>')
