n, k = map(int, input().split())
arr = []

for i in range(1, int(n**0.5)+1):
    if not n % i:
        arr.append(i)
        arr.append(n//i)

arr = list(set(arr))
arr.sort()

if k > len(arr):
    print(0)
else:
    print(arr[k-1])
