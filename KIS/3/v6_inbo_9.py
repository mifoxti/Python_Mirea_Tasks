from math import exp, floor


def main(n, m, z, a, b, p):
    sum1 = 0
    for j in range(1, m + 1):
        sum2 = 0
        for k in range(1, n + 1):
            sum2 += j ** 12 + 76 * z ** 7 + k ** 2
        sum1 += sum2

    minussum = 0
    for k in range(1, m + 1):
        minussum2 = 0
        for i in range(1, b + 1):
            minussum3 = 1
            for j in range(1, a + 1):
                minussum3 *= ((57 * i ** 2 + 35 * j ** 3) ** 7
                              - exp(k ** 2 / 47) ** 4 - 35 * floor(p))
            minussum2 += minussum3
        minussum += minussum2

    return sum1 + minussum


print(main(4, 3, 0.32, 7, 7, 0.28))  # ≈ 1.80e+184
print(main(3, 4, 0.51, 4, 3, -0.35))  # ≈ 1.97e+86
print(main(4, 7, -0.68, 7, 7, -0.33))  # ≈ 4.21e+184
print(main(2, 2, -0.39, 7, 6, -0.09))  # ≈ 2.81e+180
print(main(4, 7, 0.34, 3, 6, 0.35))  # ≈ 9.85e+71
