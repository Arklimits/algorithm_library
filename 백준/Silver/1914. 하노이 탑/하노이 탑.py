def move(start, end):
    print(start, end)


def hanoi(start, via, end, circle):
    if circle == 1:
        move(start, end)
    else:
        hanoi(start, end, via, circle-1)
        move(start, end)
        hanoi(via, start, end, circle-1)


n = int(input())

print(2**n-1)
if n <= 20:
    hanoi('1', '2', '3', n)
