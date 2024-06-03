def main(b, a, z, m, n):
    sum1 = 0
    for k in range(1, a + 1):
        sum12 = 0
        for i in range(1, b + 1):
            sum12 += (k ** 7 + 22 * (26 * z ** 3 + i ** 2 / 2) + 18)
        sum1 += sum12

    sum2 = 0
    for c in range(1, n + 1):
        sum21 = 0
        for j in range(1, m + 1):
            sum22 = 0
            for k in range(1, a + 1):
                sum22 += j ** 7 - (67 * c ** 2 - k - 56)
            sum21 += sum22
        sum2 += sum21
    return sum1 - sum2
