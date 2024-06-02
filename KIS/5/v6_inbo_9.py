from math import ceil


def main(y, z):
    n = len(y)
    r = 0
    for i in range(1, n + 1):
        r += (1 + y[ceil(i / 2 - 1)] + 67 * (z[i - 1]) ** 3) ** 2
    return 77 * r
