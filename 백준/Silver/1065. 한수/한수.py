n = int(input())

if n < 100:
    print(n)
else:
    cnt = 99
    for i in range(100, n + 1):
        i_str = str(i)
        a = int(i_str[0])
        b = int(i_str[1])
        c = int(i_str[2])
        if c - b == b - a:
            cnt += 1

    print(cnt)