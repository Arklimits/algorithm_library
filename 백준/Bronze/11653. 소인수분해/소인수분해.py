n = int(input())
if n == 1:
    exit()

arr = [0] * 2 + [1] * (n - 1)

for i in range(2, int(n**0.5)+1):
    if arr[i]:
        for j in range(i+i, n+1, i):
            arr[j] = 0

if arr[n]:
    print(n)
    exit()

dummy = n
while 1:
    for i in range(2, n+1):
        if arr[i]:
            if not dummy % i:
                print(i)
                dummy //= i
                break

    if dummy == 1:
        break
