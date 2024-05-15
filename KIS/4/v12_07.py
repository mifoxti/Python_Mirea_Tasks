from math import ceil


def main(n):
    if n == 0:
        return -0.89
    elif n >= 1:
        return main(n - 1) ** 2 - ceil(main(n - 1))


print(main(8))
