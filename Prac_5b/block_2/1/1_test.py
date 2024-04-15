# test_encoding_decoding.py
import pytest
from encoding_decoding import encode_rle, decode_rle, triangle_type
'''
@pytest.mark.parametrize("data, expected", [
    (b'AAAABBBCCDAA', b'\x04A\x03B\x02C\x01D\x02A'),
    (b'WWWWWWWWWW', b'\x0AW'),
    (b'Z', b'\x01Z'),
])
def test_encode_rle(data, expected):
    assert encode_rle(data) == expected

@pytest.mark.parametrize("data, expected", [
    (b'\x04A\x03B\x02C\x01D\x02A', b'AAAABBBCCDAA'),
    (b'\x0AW', b'WWWWWWWWWW'),
    (b'\x01Z', b'Z'),
])
def test_decode_rle(data, expected):
    assert decode_rle(data) == expected

@pytest.mark.parametrize("points, expected", [
    ((0, 0, 1, 1, 2, 0), "разносторонний"),
    ((0, 0, 0, 1, 1, 0), "равнобедренный"),
    ((0, 0, 1, 1, 0, 2), "равносторонний"),
])

@pytest.mark.parametrize("data, expected", [
    (b'AAAABBBCCDAA', b'\x04A\x03B\x02C\x01D\x02A'),  # правильный тест
    (b'WWWWWWWWWW', b'\x0BW'),  # неправильное ожидание
    (b'Z', b'\x02Z'),  # неправильное ожидание
])

@pytest.mark.parametrize("points, expected", [
    ((0, 0, 1, 1, 2, 0), "разносторонний"),   # правильные данные
    ((0, 0, 0, 1, 1, 0), "равнобедренный"),    # правильные данные
    ((0, 0, 1, 1, 0, 2), "равносторонний"),    # правильные данные
    ((0, 0, 1, 1, 2, 0, 3, 3), None),          # неверное количество координат
    ((0, 0, 1, 1, 2), None),                   # недостаточное количество координат
    ((0, 0, 0, 0, 0, 0), None),                # нулевая площадь треугольника
])
def test_triangle_type(points, expected):
    if expected is None:
        with pytest.raises(ValueError):
            triangle_type(*points)
    else:
        assert triangle_type(*points) == expected
        '''


# test_encoding_decoding.py
import pytest
from encoding_decoding import triangle_type

@pytest.mark.parametrize("points, expected", [
    ((0, 0, 1, 1, 2, 0), "разносторонний"),   # правильные данные
    ((0, 0, 0, 1, 1, 0), "равнобедренный"),    # правильные данные
    ((0, 0, 1, 1, 0, 2), "равносторонний"),    # правильные данные
    ((0, 0, 1, 1, 2), None),                   # неверное количество координат
    ((0, 0, 1, 1, 2, 0, 3, 3), None),          # слишком много координат
    ((0, 0, 0, 0, 0, 0), None),                # нулевая площадь
])
def test_triangle_type(points, expected):
    if expected is None:
        with pytest.raises(ValueError):
            triangle_type(*points)
    else:
        assert triangle_type(*points) == expected
