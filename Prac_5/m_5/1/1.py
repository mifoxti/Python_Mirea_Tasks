from hypothesis import given
from hypothesis.strategies import floats

# Импортируем функцию distance из вашего модуля
from distance import distance


# Напишем тест, используя генераторы данных от hypothesis
@given(floats(), floats(), floats(), floats())
def test_distance(x1, y1, x2, y2):
    # Вычисляем ожидаемый результат для сравнения
    expected = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    # Вызываем функцию distance и проверяем результат
    assert distance(x1, y1, x2, y2) == expected


# Запускаем тест
test_distance()
