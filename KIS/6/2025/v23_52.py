import math


def main(y):
    n = len(y)
    total_sum = 0.0
    for i in range(1, n + 1):
        ceil_val = math.ceil(i / 4)
        term = abs(y[n - ceil_val] - 1 - y[n - ceil_val] ** 2)
        total_sum += 92 * term
    return 22 * total_sum


print(main([-0.61, -0.32, 0.5, 0.56, -0.8, 0.9, 0.34, -0.16]))
print(main([0.25, 0.19, -0.22, 0.57, 0.13, -0.51, 0.24, -0.06]))
print(main([-0.43, 0.49, 0.0, -0.19, -0.77, 0.46, 0.48, -0.28]))
print(main([-0.37, -0.66, -0.97, 0.04, -0.5, -0.01, -0.84, 0.01]))
print(main([0.58, 0.8, -0.1, -0.66, -0.54, 0.66, -0.57, -0.14]))