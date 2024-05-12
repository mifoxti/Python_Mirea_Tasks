import math


def main(z, x, y):
    term1 = math.sqrt(((61 * x ** 2 - 33 * y ** 3) ** 2 / 71)
                      - (92 * z ** 2) ** 4)
    term2 = (((99 - 87 * y - x ** 2) ** 4 - math.log2(z / 68 + 24))
             / (77 * (1 - y ** 2 - z ** 3 / 80) ** 5 + 93 * x ** 2))
    result = term1 - term2
    return result


# Пример использования функции
result = main(0.16, -0.86, -0.4)
print(result)
print(main(0.15, 0.83, -0.38))  # ≈ -3.00e+06
print(main(-0.05, 0.87, -0.55))  # ≈ -5.48e+06
print(main(-0.05, 0.23, -0.4))  # ≈ -8.62e+06
print(main(-0.07, -0.57, 0.14))  # ≈ -5.60e+05
