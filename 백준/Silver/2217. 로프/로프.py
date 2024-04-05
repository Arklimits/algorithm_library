import sys


def greedy(arr):
    arr.sort(reverse=True)
    maximum = 0
    
    for i in range(N):
        if maximum < arr[i] * (i+1):
            maximum = arr[i] * (i+1)

    print(maximum)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ARR = [int(sys.stdin.readline()) for _ in range(N)]

    greedy(ARR)
