from math import exp


def main(a, b, n):
    result = 0
    for k in range(1, n + 1):
        inner_sum = 0
        for j in range(1, b + 1):
            sum3 = 0
            for i in range(1, a + 1):
                sum3 += (j ** 2 - exp(i) ** 4 / 41
                         - 30 * (j ** 2 + 1 + k) ** 3)

            inner_sum += sum3
        result += inner_sum
    return result


result = f(3, 6, 3)
print(f'{result:.2e}')
