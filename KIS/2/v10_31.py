import math


def main(z):
    if z < 11:
        return 2 * (z / 40 - 1 - z ** 2) ** 4 + z ** 7 + 82
    elif 11 <= z < 34:
        return (z ** 4) / 99 + z ** 3
    elif z >= 34:
        return 4 - (82 * z ** 3 - 45 * z) ** 3

print(f'= {main(85):.2e}')