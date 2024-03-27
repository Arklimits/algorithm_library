import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    n_arr = set(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    m_arr = list(map(int, sys.stdin.readline().split()))

    for i in m_arr:
        if i in n_arr:
            print(1, end=' ')
        else:
            print(0, end=' ')
