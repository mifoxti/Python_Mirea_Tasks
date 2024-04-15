def f(x):
    n = len(x)
    result = 0
    for i in range(1, n + 1):
        inner_sum = (0.08 + x[n - i] ** 3 + x[i - 1] / 50) ** 6 / 96
        result += inner_sum
    result *= 67
    return result


# Примеры результатов вычислений
examples = [
    ([0.26, 1.0], 1.14e+00),
    ([-0.8, -0.88], 4.44e-02),
    ([-0.66, -0.33], 6.72e-05),
    ([0.87, -0.79], 1.02e-01),
    ([0.11, -0.08], 3.87e-07)
]

# Проверка результатов
for example, expected_result in examples:
    result = f(example)
    print(f"f({example}) ≈ {result:.2e}, ожидается ≈ {expected_result:.2e}")
