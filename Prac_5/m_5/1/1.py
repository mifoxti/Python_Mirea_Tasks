from hypothesis import given
from hypothesis.strategies import floats

from distance import distance

# Ограничиваем диапазон значений точек
point_strategy = floats(min_value=-1000, max_value=1000)


@given(floats(), floats(), floats(), floats())
def test_distance(x1, y1, x2, y2):
    # Проверяем, что расстояние неотрицательное
    assert distance(x1, y1, x2, y2) >= 0

    # Проверяем свойство симметричности
    assert distance(x1, y1, x2, y2) == distance(x2, y2, x1, y1)

    # Проверяем свойство транзитивности
    if x1 == x2 and y1 == y2:
        assert distance(x1, y1, x2, y2) == 0
    else:
        x3, y3 = 2 * x2, 2 * y2
        assert distance(x1, y1, x3, y3) == 2 * distance(x1, y1, x2, y2)


test_distance()
