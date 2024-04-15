from math import log


def main(n):
    if n == 0:
        return 0.67
    elif n == 1:
        return 0.76
    elif n >= 2:
        return 50 * log(main(n - 2) ** 3 + 3 + 87 * main(n-1)) ** 2


