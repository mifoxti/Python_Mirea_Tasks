import math


def main(a, n, b, x):
    total_sum = 0.0
    for i in range(1, b + 1):
        for j in range(1, n + 1):
            for k in range(1, a + 1):
                term = (85 * math.sqrt(i)
                        - (x ** 2 / 55 + k ** 3 + j) ** 2)
                total_sum += term
    return total_sum
