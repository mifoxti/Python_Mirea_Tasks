import math


def main(n, z, a, y):
    result = 0
    for i in range(1, n + 1):
        inner_sum = math.sqrt(z) ** 6 + 79 * (math.exp(i)) ** 3
        result += inner_sum

    for c in range(1, n + 1):
        for i in range(1, a + 1):
            inner_sum = (22 * i ** 3 - c ** 2 +
                         ((y ** 3 + 8 * i ** 2) ** 7) / 85 + 43)
            result += inner_sum
    return result


n_value = 2
z_value = 0.74
a_value = 8
y_value = 0.87
result = main(n_value, z_value, a_value, y_value)
print(f"f({n_value}, {z_value}, {a_value}, {y_value}) = {result:.2e}")
