import sys
from collections import deque


def greedy():
    number = ['' for _ in range(25)]
    operator = deque()

    n = 0
    while TEXT:
        target = TEXT.popleft()

        if '0' <= target <= '9':
            number[n] += target
        else:
            n += 1
            operator.append(target)

    for i in range(25):
        if number[i] == '':
            number[i] = 0
        else:
            # noinspection PyTypeChecker
            number[i] = int(number[i])

    idx = 0
    while operator:
        oper = operator.popleft()
        idx += 1
        if oper == '-':
            number[idx] = -abs(number[idx])
            while operator:
                operator.popleft()
                idx += 1
                number[idx] = -abs(number[idx])
    
    print(sum(number))


if __name__ == '__main__':
    TEXT = deque(list(map(str, sys.stdin.readline().strip().rstrip())))

    greedy()
