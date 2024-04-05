import sys


read = sys.stdin.readline


# 구동부
def pre(pivot):
    print(pivot, end='')
    if NODE[pivot][0] != '.':
        pre(NODE[pivot][0])
    if NODE[pivot][1] != '.':
        pre(NODE[pivot][1])


def inord(pivot):
    if NODE[pivot][0] != '.':
        inord(NODE[pivot][0])
    print(pivot, end='')
    if NODE[pivot][1] != '.':
        inord(NODE[pivot][1])


def post(pivot):
    if NODE[pivot][0] != '.':
        post(NODE[pivot][0])
    if NODE[pivot][1] != '.':
        post(NODE[pivot][1])
    print(pivot, end='')


def program():
    for i in range(N):
        x, l, r = read().split()
        NODE[x] = (l, r)

    pre('A')
    print()
    inord('A')
    print()
    post('A')


# 선언부
N = int(read())
NODE = {}

program()
