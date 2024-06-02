from math import log, sqrt


def main(x):
    a = (x ** 2 + 1 + 95 * x) ** 2
    b = log(x / 30 - 96 * x ** 3, 10) ** 2 - 89 * x
    c = (4 - 33 * x ** 3) ** 6
    return a - sqrt(b / c)


print(f'= {main(-0.29):.2e}')
print(f'= {main(-0.62):.2e}')
print(f'= {main(-0.96):.2e}')
print(f'= {main(-0.32):.2e}')
print(f'= {main(-0.92):.2e}')
