import sys
from collections import deque, Counter

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_arr = {}
    arr = list(map(int, sys.stdin.readline().split()))
    for i in arr:
        if i in n_arr:
            n_arr[i] += 1
        else:
            n_arr[i] = 1

    m = int(sys.stdin.readline())
    m_arr = list(map(int, sys.stdin.readline().split()))

    m_arr = deque(m_arr)

    while m_arr:
        i = m_arr.popleft()

        if i in n_arr:
            print(n_arr[i], end=' ')
        else:
            print(0, end=' ')
