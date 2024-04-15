# -*- coding: utf-8 -*-

import pytest

# Функция для вычисления значения выражения
def evaluate_expression(x, y):
    return ((y | 7 if x <= 1 else x << 2) +
            (x if y <= 10 else 2) +
            (5 if y > 1 else y >> 8)) - (y & 10)

# Тесты
@pytest.mark.parametrize("x, y, expected_result", [
    (0, 0, 13),    # ((0 | 7) + 0 + 5) - 0 = 12 + 1 = 13
    (1, 5, 7),     # ((5 | 7) + 1 + 5) - 0 = 12 + 1 = 13
    (2, 15, 15),   # ((15 | 7) + 2 + 5) - 10 = 22 + 2 + 5 - 10 = 19
    (3, 3, 17),    # ((3 | 7) + 3 + 5) - 2 = 7 + 3 + 5 - 2 = 13
    (4, 10, 22),   # ((10 | 7) + 4 + 5) - 10 = 15 + 4 + 5 - 10 = 14
])
def test_expression_evaluation(x, y, expected_result):
    assert evaluate_expression(x, y) == expected_result
