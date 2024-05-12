from math import cos


def main(n):
    if n == 0:
        return -0.58
    elif n == 1:
        return -0.99
    elif n >= 2:
        return ((main(n - 1) ** 3) / 4 + 1 +
                (main(n - 1) / 26) + (cos(main(n - 2)) ** 2) / 55)


results = [4,
           5,
           6,
           2,
           3]
for string in results:
    print(f'= {main(string):.2e}')
