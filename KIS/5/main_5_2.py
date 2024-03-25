import math


# С использованием генератора списка:
def main(z, x, y):
    n = len(z)
    result = sum((5 * y[i - 1] - z[n - math.ceil(i / 3)] ** 2
                  - x[n - math.ceil(i / 3)] ** 3)
                 ** 6 for i in range(1, n + 1))
    return result


z_vector = [0.07, -0.22, -0.23, -0.37, 0.87, 0.82, -0.78]
x_vector = [0.02, 0.2, -0.78, -0.26, -0.35, 0.42, -0.88]
y_vector = [0.01, -0.68, 0.62, -0.14, 0.21, 0.34, 0.8]

result = main(z_vector, x_vector, y_vector)
print("Результат:", '{:.2e}'.format(result))
