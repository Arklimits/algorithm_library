import sys

read = sys.stdin.readline


def program(jump):
    removed = []

    for i in range(n):
        removed.append(str(queue.pop(jump)))
        jump += k - 1

        if not len(queue):
            break

        if jump >= len(queue):
            jump %= len(queue)

    return removed


n, k = map(int, read().split())
queue = []
for _ in range(n):
    queue.append(_+1)

print('<' + ', '.join(program(k-1)) + '>')
