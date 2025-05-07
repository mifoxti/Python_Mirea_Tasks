from math import floor, ceil, exp


def main(z):
    sum = 0
    n = len(z)
    for i in range(1, n + 1):
        sum += 78 * exp(z[n - i] - z[ceil(i / 3 - 1)]
                        ** 3 / 44 - z[n - i] ** 2) ** 4
    return sum


data = ([0.93, 0.03, 0.19, -0.55])

print(f'= {main(data):.2e}')
