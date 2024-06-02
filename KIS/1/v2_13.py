from math import sin, tan, floor


def main(z, x, y):
    a = 72 * (y ** 3 - z) ** 6 - (sin(9 * x + x ** 3 + z ** 2)) ** 3
    b = 41 * (z - y ** 2) ** 2 + 96 * (tan(19 - z ** 3 / 96 - x)) ** 6
    c = floor(65 * y ** 3 - 58 * z - x ** 2)
    d = a - b / c
    return d


print(f'= {main(0.88, -0.24, -0.24):.2e}')
print(f'= {main(0.65, 0.76, 0.12):.2e}')
print(f'= {main(-0.32, -0.88, -0.6):.2e}')
print(f'= {main(0.58, 0.88, -0.73):.2e}')
print(f'= {main(0.65, -0.63, -0.58):.2e}')