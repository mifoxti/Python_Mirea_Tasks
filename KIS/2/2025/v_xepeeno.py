import math


def main(y):
    if y < 36:
        return 52 * y
    elif 36 <= y < 72:
        return 24 * y ** 2 - ((y ** 2 - y ** 3) ** 4 / 49)
    elif 72 <= y < 172:
        return y ** 21 + y ** 3 + 1
    else:
        return 15 * y ** 7 - 42 * (math.log10(y)) ** 6


# Примеры вычислений
print(main(171))  # ≈ 7.81e+46
print(main(59))  # ≈ -3.39e+19
print(main(141))  # ≈ 1.36e+45
print(main(148))  # ≈ 3.76e+45
print(main(188))  # ≈ 1.25e+17
