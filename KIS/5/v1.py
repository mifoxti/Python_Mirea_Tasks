import math


def main(x, y, z):
    result = 0
    n = len(x)
    for i in range(1, n + 1):
        result += 8 * (y[i - 1] ** 3
                       + (x[n - math.ceil(i / 2)] ** 2) / 82 + z[i - 1])
    return result

# Данные векторы
x = [0.99, -0.32, -0.48, 0.58]
y = [-0.51, 0.78, -0.2, 0.01]
z = [0.65, -0.45, -0.52, 0.5]

# Вызов функции и вывод результата
result = f(x, y, z)
print("Результат f(x, y, z) ≈ {:.2e}".format(result))