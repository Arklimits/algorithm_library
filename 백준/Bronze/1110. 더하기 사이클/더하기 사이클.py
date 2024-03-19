n = int(input())
count = 0
if n < 10:
    n *= 10

s = n
while 1:
    count += 1
    a = s // 10
    b = s % 10
    s = a + b
    s = (b * 10) + s % 10

    if n == s:
        break

print(count)
