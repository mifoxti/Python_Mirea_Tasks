from math import sin


def main(b, n, a, x):
    sum1 = 0
    for i in range(1, n + 1):
        sum2 = 0
        for k in range(1, b + 1):
            sum2 += 54 * (52 * i ** 3 - k / 86) ** 3
        sum1 += sum2

    minussum = 0
    for j in range(1, b + 1):
        minussum2 = 0
        for k in range(1, a + 1):
            minussum3 = 0
            for c in range(1, n + 1):
                minussum3 += sin(k) ** 3 + (91 * j ** 2 + 74 * c ** 3) ** 5 + x
            minussum2 += minussum3
        minussum += minussum2

    return sum1 - minussum


print(main(5, 2, 4, 0.93))  # ≈ -1.27e+18
print(main(6, 5, 2, 0.09))  # ≈ -1.97e+21
print(main(7, 8, 8, -0.57))  # ≈ -6.59e+24
print(main(5, 6, 8, 0.48))  # ≈ -6.29e+22
print(main(5, 3, 5, 0.93))  # ≈ -1.26e+19
