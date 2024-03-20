m = int(input())
n = int(input())

arr = [1] * (n + 1)
arr[0] = arr[1] = 0

for i in range(2, int(n**0.5)+1):
    for j in range(2, n):
        if i*j > n:
            break
        arr[i*j] = 0

result = 0
for i in range(m, n+1):
    if arr[i]:
        result += i

if result:
    print(result)

    for i in range(m, n+1):
        if arr[i]:
            print(i)
            exit()

print(-1)