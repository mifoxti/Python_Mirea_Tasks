from math import ceil, sin


def main(z):
    n = len(z)
    total_sum = 0
    for i in range(1, n + 1):
        index = n + 1 - ceil(i / 2)
        z_term = z[index - 1]
        inner_expression = (53 * z_term ** 3 - 9 * z_term - 88 * z_term ** 2)
        total_sum += sin(inner_expression) ** 6 / 86
    return total_sum


# Test cases
print(main([-0.09, 0.17, 0.94]))  # Should output a value close to 2.09e-02
print(main([-0.77, 0.65, -0.95]))  # Should output a value close to 7.30e-07
print(main([-0.17, -0.93, -0.93]))  # Should output a value close to 1.53e-04
print(main([0.33, 0.11, 0.67]))  # Should output a value close to 2.60e-02
print(main([0.89, -0.84, -0.56]))  # Should output a value close to 6.39e-03
