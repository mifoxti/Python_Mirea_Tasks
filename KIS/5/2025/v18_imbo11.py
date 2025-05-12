import math


def main(x, z, y):
    n = len(x)
    total_sum = 0.0

    for i in range(1, n + 1):
        term = (y[n - math.ceil(i / 2)] ** 3
                - 69 * x[i - 1] ** 2 - z[i - 1])
        total_sum += 31 * (term) ** 6

    return total_sum


print(main([-0.53, 0.57, -0.85],
           [-0.75, -0.81, 0.64],
           [-0.95, -0.68, -0.92]))
