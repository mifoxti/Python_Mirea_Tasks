import math


def main(x, z, y):
    n = len(x)
    result = 0
    for i in range(1, n + 1):
        result += 11 * (z[n - math.ceil(i / 3)] ** 3 / 37 +
                        y[n - math.ceil(i / 2)] ** 2 + 62 * x[i - 1]) ** 6
    return result


# Пример использования
x = [-0.56, -0.69, 0.59, -0.91, 0.13, 0.6, 0.79]
y = [0.95, -0.47, 0.72, 0.17, -0.3, 0.2, -0.82]
z = [0.53, -0.45, 0.52, 0.96, 0.26, 0.64, -0.07]

result = main(x, z, y)
print("Результат f(x, z, z) = {:.2e}".format(result))
