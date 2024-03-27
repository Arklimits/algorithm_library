import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr.sort(key=lambda x: (x[0], x[1]))

    for i in range(n):
        print(*arr[i])
