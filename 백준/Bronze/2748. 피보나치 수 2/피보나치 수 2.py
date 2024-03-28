import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    ARR = [0, 1]

    for i in range(2, N+1):
        ARR.append(ARR[i-2] + ARR[i-1])

    print(ARR[-1])