def program():
    n, k = map(int, input().split())

    num = 0
    for n in range(1, n + 1):
        num = (k + num) % n

    print(num + 1)

program()