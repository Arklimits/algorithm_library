m, n = map(int, input().split())
arr = []

for i in range(2, n+1):
    pivot = 1

    for j in arr:
        if i % j == 0:
            pivot = 0
            break
        if j**2 > i:
            break

    if pivot:
        arr.append(i)

for i in range(len(arr)):
    if arr[i] >= m:
        check = i
        break

for i in range(check, len(arr)):
    print(arr[i])
