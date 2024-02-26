import random


def naive_mul(x, y):
    result = 0
    for _ in range(y):
        result += x
    return result


# Тестирование с использованием случайных данных
for _ in range(10):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    expected_result = x * y
    assert naive_mul(x, y) == expected_result

print("Тесты пройдены успешно!")


def russian_peasant_multiply(a, b):
    result = 0
    while a > 0:
        if a % 2 != 0:
            result += b
        a //= 2
        b *= 2
    return result


# Тестирование с использованием случайных данных
for _ in range(10):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    expected_result = x * y
    assert russian_peasant_multiply(x, y) == expected_result

print("Тесты пройдены успешно!")
