import math


def f(a, m, n, x):
    result = 1
    for c in range(1, n + 1):
        inner_sum = 0
        for i in range(1, m + 1):
            inner_sum += sum(
                (43 * math.tan(x) ** 6 + math.log(c) ** 7
                 + (math.cos(k - 29 * i ** 2) ** 5) / 37)
                for k in range(1, a + 1)
            )
        result *= inner_sum
    return result


# Пример использования
a = 6
m = 6
n = 3
x = -0.29
result = f(a, m, n, x)
print(f'= {result:.2e}')
