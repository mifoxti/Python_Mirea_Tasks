import math


def main(a, n, b):
    total = 0.0
    for k in range(1, b + 1):
        for i in range(1, n + 1):
            for j in range(1, a + 1):
                term = (math.exp(i) ** 3 + j ** 3
                        + (i ** 2 / 12) + k)
                total += term
    return total


# Примеры вычислений
print(main(7, 3, 2))  # ≈ 1.24e+05
print(main(4, 6, 5))  # ≈ 1.38e+09
print(main(7, 3, 3))  # ≈ 1.86e+05
print(main(6, 5, 2))  # ≈ 4.13e+07
print(main(7, 6, 7))  # ≈ 3.39e+09
