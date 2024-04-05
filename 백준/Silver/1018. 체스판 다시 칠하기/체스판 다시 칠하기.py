import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
    res = sys.maxsize

    for by in range(N-7):
        for bx in range(M-7):
            count1, count2 = 0, 0
            for y in range(8):
                for x in range(8):
                    if (y + x) % 2 == 0:
                        if arr[by + y][bx + x] != 'B':
                            count1 += 1
                    else:
                        if arr[by + y][bx + x] != 'W':
                            count1 += 1
                    if (y + x) % 2 == 0:
                        if arr[by + y][bx + x] != 'W':
                            count2 += 1
                    else:
                        if arr[by + y][bx + x] != 'B':
                            count2 += 1
            res = min(res, count1, count2)

    print(res)
