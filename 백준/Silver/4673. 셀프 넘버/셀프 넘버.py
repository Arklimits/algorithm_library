number = [1 for i in range(0, 10000)]

for i in range(1, 10000):
    pivot = str(i)
    temp = 0
    for j in pivot:
        temp += int(j)
    if int(pivot)+temp <= 10000:
        number[int(pivot)+temp-1] = 0

for i in range(10000):
    if number[i]:
        print(i+1)
        