import sys

if __name__ == '__main__':
    s = list(map(str, sys.stdin.readline().strip()))
    n = len(s)
    _set_ = set()

    for i in range(n+1):
        for j in range(i+1, n+1):
            if ''.join(s[i:j]) not in _set_:
                _set_.add(''.join(s[i:j]))

    print(len(_set_))