import random


def bucketsort(arr, k):
    # �������� �� ������ ������
    if not arr:
        return []

    # �������� �������� ��� ������� ��������
    counts = [0] * k
    for x in arr:
        # ��������, ��� ������� ������� ������������� ��������� ���������
        assert 0 <= x < k, "������� ������� �� ������ � �������� [0, k-1]"
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


def test_bucketsort():
    # ������������ ������� �������
    assert bucketsort([], 5) == []

    # ������������ ������� � ����� ���������
    assert bucketsort([3], 5) == [3]

    # ������������ ��������� ������
    random_arr = [random.randint(0, 4) for _ in range(10)]
    sorted_arr = sorted(random_arr)
    assert bucketsort(random_arr, 5) == sorted_arr

    # ������������ ���������, ��������� �� ������� ��������� [0, k-1]
    try:
        bucketsort([5, 6, 7], 5)
    except AssertionError as e:
        assert str(e) == "������� ������� �� ������ � �������� [0, k-1]"


if __name__ == "__main__":
    test_bucketsort()
    print("��� ����� �������� �������!")
