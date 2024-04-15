# encoding_decoding.py
def encode_rle(data):
    encoded = bytearray()
    count = 1
    last_char = data[0]
    for i in range(1, len(data)):
        if data[i] == last_char:
            count += 1
        else:
            encoded.extend([last_char, count])
            count = 1
            last_char = data[i]
    encoded.extend([last_char, count])
    return bytes(encoded)

def decode_rle(data):
    decoded = bytearray()
    i = 0
    while i < len(data):
        count = data[i]
        char = data[i + 1]
        decoded.extend([char]*count)
        i += 2
    return bytes(decoded)

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def triangle_type(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    if a == b == c:
        return "равносторонний"
    elif a == b or a == c or b == c:
        return "равнобедренный"
    else:
        return "разносторонний"

# test_encoding_decoding.py
import pytest
from encoding_decoding import encode_rle, decode_rle, triangle_type

@pytest.mark.parametrize("data, expected", [
    (b'AAAABBBCCDAA', b'\x04A\x03B\x02C\x01D\x02A'),  # правильный тест
    (b'WWWWWWWWWW', b'\x0BW'),  # неправильное ожидание
    (b'Z', b'\x02Z'),  # неправильное ожидание
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

# Ввод с клавиатуры
def main():
    x1, y1 = map(int, input("Введите координаты первой точки (x1 y1): ").split())
    x2, y2 = map(int, input("Введите координаты второй точки (x2 y2): ").split())
    x3, y3 = map(int, input("Введите координаты третьей точки (x3 y3): ").split())

    print("Тип треугольника:", triangle_type(x1, y1, x2, y2, x3, y3))

if __name__ == "__main__":
    main()
