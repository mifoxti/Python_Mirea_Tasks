import math


def main(n):
    if n == 0:
        return -0.29
    elif n == 1:
        return -0.24
    else:
        f_prev_prev = main(n - 2)
        f_prev = main(n - 1)
        term = math.log10(f_prev + 37 * f_prev_prev ** 2)
        return f_prev_prev ** 3 + 0.01 + term


# Примеры вычислений
print(main(3))  # ≈ 4.07e-01
print(main(6))  # ≈ 2.53e+00
print(main(5))  # ≈ 9.29e-01
print(main(4))  # ≈ 9.83e-01
print(main(7))  # ≈ 2.35e+00
