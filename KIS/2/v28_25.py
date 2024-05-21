import math


def main(z):
    if z < 96:
        return (z ** 2 - 1) ** 5
    elif 96 <= z < 166:
        return ((0.11 + 75 * z ** 3) ** 6 - (z ** 2 - 84 * z) ** 7
                - 91 * z ** 5)
    elif 166 <= z < 262:
        return (61 * (z ** 3 - 1 - z) ** 7
                + 44 * z ** 3 + 81 * (73 * z ** 2 - 22 * z) ** 6)
    elif 262 <= z < 298:
        return 83 * z ** 6 - (62 * z) ** 5 / 58
    elif z >= 298:
        return 28 * math.log10(z) ** 2 + 52 * math.cos(62 * z ** 3)


# Примеры вычислений
print(f"f(51) = {main(51):.2e}")
print(f"f(246) = {main(246):.2e}")
print(f"f(153) = {main(153):.2e}")
print(f"f(299) = {main(299):.2e}")
print(f"f(129) = {main(129):.2e}")
