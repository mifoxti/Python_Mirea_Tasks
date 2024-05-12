import math


def main(a, m, b, z):
    result = 0
    for j in range(1, b + 1):
        for k in range(1, m + 1):
            for i in range(1, a + 1):
                result += (50 * i ** 3 - 50 * k ** 6
                           - 78 * (53 - j ** 2 - z) ** 4)
    return result


results = [(4, 7, 4, 0.99),
           (8, 5, 8, -0.41),
           (8, 4, 4, -0.64),
           (7, 7, 2, -0.81),
           (7, 5, 6, -0.89)]
for string in results:
    print(f'= {main(string[0], string[1], string[2], string[3]):.2e}')
