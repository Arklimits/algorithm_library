c = int(input())

for _ in range(c):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]

    cnt = 0
    for i in arr[1:]:
        if i > avg:
            cnt += 1

    print('{0:.3f}%'.format(cnt/arr[0]*100))