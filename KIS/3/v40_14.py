def main(n, m, a, y):
    result = 0
    for c in range(1, a + 1):
        mel_sum = 0
        for k in range(1, m + 1):
            mel_sum_2 = 1
            for i in range(1, n + 1):
                mel_sum_2 *= (15 * (c + y ** 2) ** 2 +
                              47 * (41 * i ** 3 +
                                    i + k ** 2) ** 7)
            mel_sum += mel_sum_2
        result += mel_sum
    return result


results = [(7, 6, 4, -0.28),
           (5, 4, 8, -0.99),
           (4, 8, 8, -0.67),
           (8, 7, 7, -0.27),
           (5, 2, 5, -0.34)]
for string in results:
    print(f'= {main(string[0], string[1], string[2], string[3]):.2e}')
