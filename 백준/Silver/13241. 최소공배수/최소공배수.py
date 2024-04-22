import sys

if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().split())

    if b > a:
        c, temp = b, a
    else:
        c, temp = a, b

    while temp != 0:
        c, temp = temp, c % temp

    print(a // c * b // c * c)
