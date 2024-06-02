from math import ceil


def main(x, y, z):
    n = len(x)
    sum = 0
    for i in range(1, n + 1):
        a = (y[ceil(i / 4) - 1] ** 3
             - 80 * x[n - i - 1] - z[ceil(i / 2) - 1] ** 2) ** 3
        sum += a / 90
    return sum


print(main([-0.45, 0.79],
           [-0.29, -0.28],
           [-0.58, 0.05]))
