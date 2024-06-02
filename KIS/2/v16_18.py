from math import log10


def main(x):
    if x < 33:
        return 1 + log10(5 * x + 74 * x ** 2) ** 5 + x ** 4
    elif 33 <= x < 48:
        return x ** 2 / 15 - 10 * (x - 1 - x ** 3) ** 4
    elif x >= 48:
        return 13 * x ** 3 + x ** 3 / 60
