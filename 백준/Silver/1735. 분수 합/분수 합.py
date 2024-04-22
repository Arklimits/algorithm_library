import sys


def LCM(a: int, b: int) -> int:
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


if __name__ == '__main__':
    a1, a2 = map(int, sys.stdin.readline().split())
    b1, b2 = map(int, sys.stdin.readline().split())

    lcm = LCM(a2, b2)

    res2 = lcm * (a2 // lcm) * (b2 // lcm)

    a1 *= b2 // lcm
    b1 *= a2 // lcm

    res1 = a1 + b1

    res_lcm = LCM(res1, res2)

    print(res1 // res_lcm, res2 // res_lcm)
