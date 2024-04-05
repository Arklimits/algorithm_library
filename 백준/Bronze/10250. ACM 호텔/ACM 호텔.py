t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    count = 1

    while n > h:
        n -= h
        count += 1

    print(str(n)+str(count).zfill(2))
