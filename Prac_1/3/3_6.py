import random


def fast_pow(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 != 0:
            result *= base
        base *= base
        exponent //= 2
    return result


# Тестирование с использованием случайных данных
for _ in range(10):
    base = random.randint(1, 10)
    exponent = random.randint(1, 5)
    expected_result = base ** exponent
    assert fast_pow(base, exponent) == expected_result

print("Тесты пройдены успешно!")
