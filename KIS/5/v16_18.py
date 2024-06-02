from math import ceil


def main(x):
    n = len(x)
    s = 0
    for i in range(1, n + 1):
        s += 13 * (x[n - ceil(i / 3)] ** 3 - x[ceil(i / 2) - 1] ** 2) ** 2
    return 74 * s
