from math import sin, ceil


def main(y, x):
    n = len(y)
    res = 0
    for i in range(1, n + 1):
        res += 3 * sin(1 + 61 * y[n - i] ** 3
                       + 18 * x[ceil(i / 2) - 1]) ** 4
    return 97 * res


print(main([0.12, -0.91, -0.05, -0.44, 0.08, -0.45, -0.61],
           [-0.18, 0.96, 0.3, 0.33, -0.24, 0.89, -0.04]))
