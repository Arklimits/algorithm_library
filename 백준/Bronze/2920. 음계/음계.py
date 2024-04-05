arr = list(map(int, input().split()))

asc = 0
dsc = 0

for i in range(8):
    if arr[i] == i+1:
        asc += 1
    if arr[i] == 8-i:
        dsc += 1

if asc == 8:
    print('ascending')
elif dsc == 8:
    print('descending')
else:
    print('mixed')
