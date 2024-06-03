from math import sqrt, log2


def main(y, x, z):
    a = 8 * y ** 9 - log2(z ** 3 - x ** 2 / 77 - z) ** 7
    b = z ** 4 + (z ** 3 / 33 - x - 51 * y ** 2) ** 5
    c = y - x ** 2 + 42 * (x - z ** 2 / 74 - 9 * y ** 3) ** 4
    d = y ** 5 - 58 * (6 * z - 50 * x ** 3 - 21) ** 3
    print(a / b - sqrt(c / d))
    return a / b - sqrt(c / d)


main(0.69, -0.27, -0.01)
main(-0.88, 0.35, -0.82)
main(0.11, -0.62, -0.34)
main(-0.75, 0.22, -0.24)
main(-0.82, 0.44, -0.05)