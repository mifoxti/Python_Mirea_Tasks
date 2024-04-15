import math


def main(n):
    if n == 0:
        return -0.15
    elif n == 1:
        return -0.31
    elif n >= 2:
        return 1 - main(n - 1) / 13 - abs(main(n - 2)) ** 3
   