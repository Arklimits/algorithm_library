import sys # 실패


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)

    if not DP[a][b][c]:
        if a < b < c:
            DP[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            DP[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return DP[a][b][c]


def dynamic(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print(f"w({a}, {b}, {c}) = 1")
        return

    ans = w(a, b, c)

    print(f"w({a}, {b}, {c}) = {ans}")


if __name__ == '__main__':
    DP = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

    while 1:
        A, B, C = map(int, sys.stdin.readline().split())

        if A == B == C == -1:
            break

        dynamic(A, B, C)
