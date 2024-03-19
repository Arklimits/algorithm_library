n = int(input())

check = n
result = int(1e10)
p = 0
_5kg = n // 5
n %= 5

if n % 3 != 0:
    for i in range(_5kg + 1):
        if (check - i * 5) % 3 == 0:
            result = min(result, (i + ((check - i * 5) // 3)))
            p = 2
else:
    _3kg = n // 3
    p = 1
    print(_5kg+_3kg)

if p == 2:
    print(result)
elif not p:
    print(-1)
