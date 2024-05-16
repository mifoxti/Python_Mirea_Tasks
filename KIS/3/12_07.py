def f(n, b, a):
    result = 1
    for k in range(1, a + 1):
        inner_sum = 1
        for i in range(1, b + 1):
            inner_sum *= sum(
                (1 + i + 95 * k ** 3 - 8 *
                 (20 + (j ** 3 / 90)) ** 2
                 - i ** 5)
                for j in range(1, n + 1)
            )
        result *= inner_sum
    return result


result = f(3, 6, 3)
print(f'{result:.2e}')
