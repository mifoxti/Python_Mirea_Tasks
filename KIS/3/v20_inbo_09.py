import math


def main(a, n, b, z):
    result = 0
    for j in range(1, b + 1):
        for k in range(1, n + 1):
            for c in range(1, a + 1):
                result += (j ** 2 + z + (43 - k
                                         - 40 * c ** 2) ** 7)

    return result


results = [(6, 6, 5, -0.4),
           (2, 4, 3, 0.86),
           (2, 5, 4, 0.12),
           (4, 4, 5, -0.14),
           (7, 3, 8, -0.8)]
for string in results:
    print(f'= {main(string[0], string[1], string[2], string[3]):.2e}')
