from math import atan


def main(n):
    if n == 0:
        return -0.17
    elif n == 1:
        return -0.45
    elif n >= 2:
        return atan(main(n - 1)) ** 2 + main(n - 2) + 67
