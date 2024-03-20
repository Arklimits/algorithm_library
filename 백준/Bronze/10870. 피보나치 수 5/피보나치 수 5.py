n = int(input())
num1 = 0
num2 = 1
if n == 0:
    print(0)
    exit()
if n < 3:
    print(1)
    exit()
for i in range(2, n+1):
    temp = num2
    num2 = num1 + num2
    num1 = temp

print(num2)