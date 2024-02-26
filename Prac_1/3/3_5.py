import random


def fast_mul(x, y):
    result = 0
    while y > 0:
        if y % 2 != 0:
            result += x
        x <<= 1
        y >>= 1
    return result


# Тестирование с использованием случайных данных
for _ in range(10):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    expected_result = x * y
    assert fast_mul(x, y) == expected_result

print("Тесты пройдены успешно!")
