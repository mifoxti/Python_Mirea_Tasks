import math


def main(y, x):
    n = len(y)
    total = 0.0
    for i in range(1, n + 1):
        ceil_val = math.ceil(i / 3)
        term = 41 * x[ceil_val - 1] - y[n - ceil_val] ** 3
        total += term ** 3
    return total


# Примеры вычислений
print(main([-0.49, 0.37, 0.83, 0.22, -0.32], [-0.71, 0.54, -0.7, 0.17, -0.42]))  # ≈ -5.21e+04
print(main([-0.38, -0.2, 0.42, -0.79, 0.63], [-0.58, -0.58, -0.92, 0.63, -0.76]))  # ≈ -6.69e+04
print(main([0.61, -0.69, 0.87, 0.28, 0.62], [0.64, 0.14, -0.42, -0.7, -0.01]))  # ≈ 5.31e+04
print(main([0.24, -0.12, -0.25, -0.24, -0.57], [-0.54, 0.96, -0.46, 0.63, 0.24]))  # ≈ 9.03e+04
print(main([-0.35, -0.45, 0.78, 0.79, -0.38], [0.19, -0.19, -0.06, 0.32, 0.83]))  # ≈ 3.12e+02
