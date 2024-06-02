from math import log2


def main(n):
    if n == 0:
        return -0.17
    elif n == 1:
        return -0.60
    elif n >= 2:
        return 35 * log2(main(n - 1) ** 3
                         - 89 * main(n - 1) - 1) ** 2 - main(n - 2)
