from math import ceil


def main(z, x, y):
    n = len(y)
    res = 0
    for i in range(1, n + 1):
        res += ((61 * x[ceil(i / 2) - 1] ** 2
                 - y[n - ceil(i / 2)] ** 3 - 67 * z[n - i]) ** 5) / 22
    return 32 * res
