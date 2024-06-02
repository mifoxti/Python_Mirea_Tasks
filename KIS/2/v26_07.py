from math import ceil, log2, log10, sin


def main(x):
    if x < -17:
        return (1 - 96 * x ** 2) ** 3 - 0.01
    elif -17 <= x < -3:
        return 12 * log10(x) - x ** 2 / 69
    elif -3 <= x < 23:
        return (40 - x ** 3 - x ** 2
                - 63 * (x / 44 - 8) ** 6
                - sin(98 * x ** 3 - 55 * x) ** 4 / 68)
    elif 23 <= x < 93:
        return ceil(x ** 2 - 17 * x - 17) ** 6 / 24
    elif x >= 93:
        return (log2(x / 47 + 59 * x ** 2) ** 6 - 99 * x ** 2
                - log10(x ** 3 + x + x ** 2 / 72) ** 7)


print(f'= {main(38):.2e}')
print(f'= {main(22):.2e}')
print(f'= {main(31):.2e}')
print(f'= {main(124):.2e}')
print(f'= {main(41):.2e}')
