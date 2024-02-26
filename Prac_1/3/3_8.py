import random


def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul16k(x, y):
    if x < 0 or y < 0:
        raise ValueError("Both x and y must be non-negative")

    # Базовый случай, когда числа 8-битные
    if x < 256 and y < 256:
        return mul_bits(x, y, 8)

    # Вычисляем размер половины числа
    n = max(x.bit_length(), y.bit_length()) // 2

    # Разбиваем числа на половины
    a, b = divmod(x, 2 ** n)
    c, d = divmod(y, 2 ** n)

    # Рекурсивно вычисляем три умножения
    ac = mul16k(a, c)
    bd = mul16k(b, d)
    ad_bc = mul16k(a + b, c + d) - ac - bd

    # Собираем результат по формуле Карацубы
    result = (ac << (2 * n)) + (ad_bc << n) + bd

    return result


# Тестирование с использованием случайных данных
for _ in range(10):
    x = random.randint(0, 2 ** 16 - 1)
    y = random.randint(0, 2 ** 16 - 1)
    expected_result = x * y
    assert mul16k(x, y) == expected_result

print("Тесты пройдены успешно!")
