import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = []
    n_arr = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    m_arr = list(map(int, sys.stdin.readline().split()))

    n_arr.sort()

    for i in range(m):
        start = 0
        end = n-1
        while start <= end:
            mid = (start + end) // 2
            if n_arr[mid] == m_arr[i]:
                print(1, end=' ')
                break
            elif n_arr[mid] < m_arr[i]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if n_arr[end] == m_arr[i]:
                print(1, end=' ')
            else:
                print(0, end=' ')

