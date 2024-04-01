import sys


def dynamic(arr):
    for i in range(1, M):
        arr[0][i] += arr[0][i-1]

    for i in range(1, N):
        go_right = arr[i][:]
        go_left = arr[i][:]

        go_right[0] += arr[i - 1][0]
        go_left[M - 1] += arr[i - 1][M - 1]

        for j in range(1, M):
            go_right[j] += max(arr[i-1][j], go_right[j-1])

        for j in range(M-2, -1, -1):
            go_left[j] += max(arr[i-1][j], go_left[j+1])

        for j in range(M):
            arr[i][j] = max(go_right[j], go_left[j])

    print(arr[N-1][M-1])


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    ARR = []
    for _ in range(N):
        ARR.append(list(map(int, sys.stdin.readline().split())))

    dynamic(ARR)
