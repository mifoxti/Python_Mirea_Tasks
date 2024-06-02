def main(a, b, n, z):
    res = 0
    for i in range(1, n + 1):
        sum1 = 0
        for k in range(1, b + 1):
            sum2 = 0
            for c in range(1, a + 1):
                sum2 += 48 * i ** 3 - 9 * z ** 5 - (66 + c ** 2 + k) ** 7
            sum1 += sum2
        res += sum1
    return res


print(main(8, 6, 8, -0.18))
print(main(5, 3, 5, -0.34))
print(main(2, 4, 4, -0.92))
print(main(7, 3, 7, 0.41))
print(main(6, 4, 6, 0.22))
