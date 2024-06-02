from math import exp


def main(z):
    if z < 68:
        return 1 - z ** 2
    elif 68 <= z < 115:
        return 29 * z + 90
    elif 115 <= z < 196:
        return 78 * z + exp(z ** 2 - 49 * z ** 3 - 1) ** 4
    elif 196 <= z < 265:
        return 85 * (abs(18 + z ** 3)) ** 4 - 37 * z ** 5
    elif 265 <= z:
        return 6 * (60 * z ** 2 + 1)


print(main(38))
print(main(266))
print(main(64))
print(main(122))
print(main(171))
