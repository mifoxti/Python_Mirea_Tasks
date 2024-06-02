from math import sin, log


def main(y, x, z):
    a = (y ** 3 + 12 * z + 66) ** 6 / 89 - sin(25 + z ** 2 + x ** 3)
    b = 18 * (49 - 37 * x ** 2 - z) + 91 * (1 + y) ** 6
    c = (92 * (84 * x ** 2 - x ** 3 - z) ** 4
         + log(82 * y + 46 + 67 * z ** 2) ** 2)
    return a / b - c
