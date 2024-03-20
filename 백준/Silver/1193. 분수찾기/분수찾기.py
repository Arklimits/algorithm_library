x = int(input())
n = 0
i = 1

while n < x:
    n += i
    i += 1

if i % 2:
    print(f"{x-n+i-1}/{n-x+1}")
else:
    print(f"{n-x+1}/{x-n+i-1}")
