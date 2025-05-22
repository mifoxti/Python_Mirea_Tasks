import math


def main(y, x):
    numerator = (15 * (1 - x ** 2 - x ** 3) +
                 2 * (31 * x ** 3 - 54 * y - 79 * x ** 2) ** 4)
    denominator = (98 * x ** 3 - 56 * y) ** 5
    sqrt_part = math.sqrt(numerator / denominator)
    fraction_part = (36 * y ** 3 - (x ** 2 / 75)) ** 4 / 63
    denominator_part = 36 * (x ** 2 + 44 * y +
                             83 * x ** 3) ** 2 - math.sin(x) ** 7
    result = sqrt_part + fraction_part / denominator_part
    return result


# Примеры вычислений
print(main(-0.0, 0.03))  # ≈ 1.07e+07
print(main(-0.69, -0.67))  # ≈ 3.18e-01
print(main(0.02, 0.31))  # ≈ 1.96e+01
print(main(-0.29, -0.26))  # ≈ 1.68e-01
print(main(-0.16, 0.53))  # ≈ 4.20e-02
