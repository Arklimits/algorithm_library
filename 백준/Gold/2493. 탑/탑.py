import sys
from collections import deque

read = sys.stdin.readline


def program():
    res = deque()
    stack = deque()
    pos_stack = deque()
    pos, prev = 0, 0

    for i in range(n):
        now = queue.popleft()

        if prev > now:
            stack.append(prev)
            pos_stack.append(i)
            res.append(i)
        else:
            if len(stack):
                while 1:
                    if not len(stack):
                        res.append(0)
                        break

                    erase = stack.pop()
                    pos = pos_stack.pop()

                    if erase > now:
                        stack.append(erase)
                        pos_stack.append(pos)

                        res.append(pos)
                        break

            else:
                res.append(0)

        prev = now

    for i in res:
        print(i, end=' ')


n = int(read())
queue = list(map(int, read().split()))
queue = deque(queue)

program()
