from math import log


def main(n):
    if n == 0:
        return -0.79
    elif n >= 1:
        return 77 * log(main(n - 1) ** 2 - 0.02, 2) ** 2 + 1


print(main(6))
print(main(8))
