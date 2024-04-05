import sys


def calculator(i, num):
    global maximum, minimum, pivot

    if i == n:
        if pivot:
            maximum = num
            minimum = num
            pivot = 0
        elif num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num

    else:
        if y[0] > 0:
            y[0] -= 1
            calculator(i + 1, num + a[i])
            y[0] += 1
        if y[1] > 0:
            y[1] -= 1
            calculator(i + 1, num - a[i])
            y[1] += 1
        if y[2] > 0:
            y[2] -= 1
            calculator(i + 1, num * a[i])
            y[2] += 1
        if y[3] > 0:
            y[3] -= 1
            calculator(i + 1, int(num / a[i]))
            y[3] += 1


pivot = 1
maximum = minimum = 0

n = int(sys.stdin.readline())
a = list(map(int, input().split()))
y = list(map(int, input().split()))

calculator(1, a[0])

print(maximum)
print(minimum)
