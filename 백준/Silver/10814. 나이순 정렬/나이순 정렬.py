import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = []
    for i in range(n):
        a, b = list(sys.stdin.readline().split())
        arr.append([int(a), b])

    arr.sort(key=lambda x: x[0])

    for i in range(n):
        print(*arr[i])
