t = int(input())
q = d = n = p = 0

for _ in range(t):
    money = int(input())

    q = money // 25
    money %= 25
    d = money // 10
    money %= 10
    n = money // 5
    money %= 5
    p = money

    print(q,d,n,p)

