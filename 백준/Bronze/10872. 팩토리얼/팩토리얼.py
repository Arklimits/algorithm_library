n = int(input())

if n > 0:
    for i in range(2, n):
        n = n * i

    print(n)
    
else:
    print(1)
