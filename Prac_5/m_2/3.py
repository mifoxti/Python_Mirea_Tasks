def distance(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return "������: ����� ���������!"
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# �������������� ����� ��� ������� distance
def test_distance_with_error():
    assert distance(0, 0, 0, 0) == "������: ����� ���������!"
    assert distance(1, 2, 1, 2) == "������: ����� ���������!"


if __name__ == "__main__":
    test_distance_with_error()
    print("Additional tests passed!")
