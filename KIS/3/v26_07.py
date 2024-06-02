def main(b, a, n, y):
    outer_sum = sum(74 * i ** 7 for i in range(1, b + 1))

    def inner_expression(j, k, c):
        return 34 * (15 * j - y ** 3 - 96) ** 7 - (k + c ** 2) ** 3 / 74

    product = 1
    for c in range(1, b + 1):
        inner_sum = sum(inner_expression(j, k, c)
                        for j in range(1, n + 1) for k in range(1, a + 1))
        product *= inner_sum

    result = outer_sum - product
    return result


# Test cases
print(main(2, 8, 2, -0.96))  # Should output a value close to -5.06e+31
print(main(6, 8, 3, -0.14))  # Should output a value close to -2.52e+95
print(main(4, 2, 7, -0.34))  # Should output a value close to -3.51e+61
print(main(5, 6, 4, 0.24))  # Should output a value close to 7.69e+78
print(main(7, 5, 2, -0.02))  # Should output a value close to 6.01e+109
