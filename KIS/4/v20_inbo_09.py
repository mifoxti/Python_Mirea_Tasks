from math import atan


def main(n):
    if n == 0:
        return -0.92
    elif n == 1:
        return -0.44
    elif n >= 2:
        return main(n - 1) - atan(93 * main(n - 2) + 0.02) ** 2


results = [(3),
           (5),
           (2),
           (9),
           (4)]

for string in results:
    print(f'= {main(string):.2e}')
