def prime(num):
    if num < 2:
        return 0
    else:
        for i in range(2, num):
            if num % i == 0:
                return 0

        return 1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for t in arr:
        ans += prime(t)

    print(ans)
