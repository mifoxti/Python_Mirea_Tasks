from math import ceil


def main(y, x, z):
    sum = 0
    n = len(y)
    for i in range(1, n + 1):
        sum += (z[n - ceil(i / 3)] ** 3 / 33 - x[n - ceil(i / 2)]
                - 51 * y[i - 1] ** 2) ** 4
    return sum

