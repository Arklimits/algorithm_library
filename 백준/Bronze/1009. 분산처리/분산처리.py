T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a %= 10
    
    if a == 0:
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [4, 9]:
        if b % 2 == 0:
            print((a ** 2) % 10)
        else:
            print(a)
    elif a in [2, 3, 7, 8]:
        b %= 4
        if b == 0:
            b = 4
        print((a ** b) % 10)
