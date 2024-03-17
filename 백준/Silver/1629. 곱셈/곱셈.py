import sys


def load():
    return sys.stdin.readline()


def multiply(jisu):
    if jisu == 1:
        return a % c

    k = multiply(jisu // 2) % c

    if jisu % 2:
        return k*k%c*a%c
    else:
        return k*k%c


a, b, c = map(int, load().split())

print(multiply(b))
