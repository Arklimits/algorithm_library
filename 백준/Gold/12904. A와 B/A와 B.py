import sys


def greedy(s, t):
    while s != t and len(t):
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] == 'B':
            t = t[:-1]
            t = t[::-1]
        else:
            break

    if s == t:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    S = sys.stdin.readline().rstrip()
    T = sys.stdin.readline().rstrip()

    greedy(S, T)
