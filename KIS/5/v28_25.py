from math import ceil


def main(z, y, x):
    n = len(z)
    result = 0
    for i in range(1, n + 1):
        term = (30 * x[n - ceil(i / 2)] ** 3 - 81 * z[n - i] - 3 * y[n - i] ** 2) ** 5 / 58
        result += term
    return 42 * result


# Примеры вычислений
print(
    f"f([0.47, -0.14, 0.66], [0.01, -0.17, 0.17], [0.94, -0.81, 0.76]) = {main([0.47, -0.14, 0.66], [0.01, -0.17, 0.17], [0.94, -0.81, 0.76]):.2e}")
print(
    f"f([0.94, -0.6, -0.06], [0.7, -0.49, -0.55], [-0.84, -0.45, 0.46]) = {main([0.94, -0.6, -0.06], [0.7, -0.49, -0.55], [-0.84, -0.45, 0.46]):.2e}")
print(
    f"f([-0.16, -0.59, -0.08], [-0.61, -0.28, -0.06], [0.86, 0.23, 0.53]) = {main([-0.16, -0.59, -0.08], [-0.61, -0.28, -0.06], [0.86, 0.23, 0.53]):.2e}")
print(
    f"f([0.77, -0.71, -0.87], [0.36, -0.63, -0.06], [0.84, 0.82, -0.44]) = {main([0.77, -0.71, -0.87], [0.36, -0.63, -0.06], [0.84, 0.82, -0.44]):.2e}")
print(
    f"f([-0.53, -0.88, -0.74], [-0.56, 0.04, 0.84], [0.47, -0.66, -0.5]) = {main([-0.53, -0.88, -0.74], [-0.56, 0.04, 0.84], [0.47, -0.66, -0.5]):.2e}")
