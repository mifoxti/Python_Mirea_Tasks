from math import cos


def main(y):
    res = 0
    n = len(y)
    for i in range(1, n + 1):
        res += cos(1 - 56 * y[n - i] ** 2) ** 6 / 33
    return 8 * res


