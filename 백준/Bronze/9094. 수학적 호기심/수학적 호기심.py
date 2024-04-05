import sys


def bruteforce(n, m):
    count = 0

    for a in range(1, n - 1):
        for b in range(a + 1, n):
            temp = (a * a + b * b + m) / (a * b)
            if temp == int(temp):
                count += 1

    print(count)


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())

        bruteforce(N, M)
