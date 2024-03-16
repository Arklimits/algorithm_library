import sys
from itertools import permutations


def calculator(opr, num1, num2):
    if opr == 0:
        return num1 + num2
    elif opr == 1:
        return num1 - num2
    elif opr == 2:
        return num1 * num2
    else:
        return int(num1 / num2)


pivot = 1
maximum = minimum = 0

n = int(sys.stdin.readline())
a = list(map(int, input().split()))
y = list(map(int, input().split()))
stack = []

for i in range(4):
    for j in range(y[i]):
        stack.append(i)

oper = list(permutations(stack))

for j in range(len(oper)):
    value = a[0]
    for i in range(1, n):
        value = calculator(oper[j][i-1], value, a[i])

    if pivot:
        maximum = minimum = value
        pivot = 0
    elif value > maximum:
        maximum = value
    elif value < minimum:
        minimum = value

print(maximum)
print(minimum)
