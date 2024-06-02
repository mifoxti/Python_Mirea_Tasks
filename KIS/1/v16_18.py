from math import floor, ceil


def main(y, x, z):
    a = 35 * (73 * x ** 2 + 90 * y) ** 2
    b = (ceil(39 * z - 0.02)) ** 4
    c = (z ** 2 / 2 - x ** 3 - y) ** 7 + 29 * z
    d = (floor(10 * y)) ** 4 + (z ** 2 - 97 - 24 * z ** 3) ** 2
    return a - b + c / d
