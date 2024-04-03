import sys


def greedy(arr):
    arr.sort()
    ans = [0 for _ in range(len(arr))]

    for idx, i in enumerate(arr):
        if idx == 0:
            ans[idx] = i
        else:
            ans[idx] = ans[idx-1] + i

    print(sum(ans))


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ARR = list(map(int, sys.stdin.readline().split()))

    greedy(ARR)
