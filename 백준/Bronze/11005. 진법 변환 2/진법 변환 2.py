n, b = map(int, input().split())
result = []

while n >= b:
    result.append(n % b)
    n //= b
result.append(n)

if b > 10:
    for i in reversed(result):
        if i > 9:
            i = chr(65+i-10)
        print(i, end='')

else:
    for i in reversed(result):
        print(i, end='')

