from math import sin


def main(x):
    if x < 119:
        return (87 + 68 * x) ** 2 + 46
    elif 119 <= x < 162:
        return 77 * sin(x)
    elif x >= 162:
        return 89 - 37 * x ** 7 - 3 * x ** 5
