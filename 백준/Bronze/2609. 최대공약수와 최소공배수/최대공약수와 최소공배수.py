import sys
from collections import deque


def prime_factory(num, queue):
    if num == 1:
        queue.append(1)
    else:
        i = 2
        while i != num:
            if not num % i:
                queue.append(i)
                num = num // i
            else:
                i += 1
        queue.append(num)

    return queue


if __name__ == '__main__':
    num1, num2 = map(int, sys.stdin.readline().split())

    queue1 = deque()
    queue2 = deque()

    queue1 = prime_factory(num1, queue1)
    queue2 = prime_factory(num2, queue2)

    max_div = 1
    min_mul = 1

    while queue1:
        num = queue1[0]
        if num in queue2:
            max_div *= num
            queue2.remove(num)
        queue1.remove(num)
        min_mul *= num

    while queue2:
        num = queue2[0]
        min_mul *= num
        queue2.remove(num)

    print(max_div)
    print(min_mul)
