import math


def main(z):
    if z < 34:
        return 0.02 - 10 * (math.ceil(57 - z)) ** 6 - (abs(z)) ** 4
    elif 34 <= z < 105:
        return 36 * z + 66 * (51 * (z ** 3) - 56 * z - 1) ** 2
    elif 105 <= z < 172:
        return ((63 * z) ** 7) / 28 - (z ** 2) / 15 - 57 * z
    elif 172 <= z < 236:
        return 0.02 + 53 * (39 * z ** 2 + z) ** 3
    else:
        return 96 - 43 * (94 - 98 * z ** 2) ** 3
