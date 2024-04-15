# def distance(x1, y1, x2, y2):#     return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
## # Тесты для функции distance
# def test_distance():#     assert distance(0, 0, 3, 4) == 5.0
#     assert distance(1, 1, 4, 5) == 5.0#     assert distance(0, 0, 1, 1) == 2**0.5
## if __name__ == "__main__":
#     test_distance()#     print("All tests passed!")
def distance(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:        return "Ошибка: точки совпадают!"
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
# Дополнительные тесты для функции distancedef test_distance_with_error():
    assert distance(0, 0, 0, 0) == "Ошибка: точки совпадают!"
    assert distance(1, 2, 1, 2) == "Ошибка: точки совпадают!"
if __name__ == "__main__":
    test_distance_with_error()
    print("Additional tests passed!")