import random


def bucketsort(arr, k):
    # Проверка на пустой список
    if not arr:
        return []

    # Создание счетчика для каждого элемента
    counts = [0] * k
    for x in arr:
        # Проверка, что элемент массива соответствует диапазону счетчиков
        assert 0 <= x < k, "Элемент массива не входит в диапазон [0, k-1]"
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


def test_bucketsort():
    # Тестирование пустого массива
    assert bucketsort([], 5) == []

    # Тестирование массива с одним элементом
    assert bucketsort([3], 5) == [3]

    # Тестирование случайных данных
    random_arr = [random.randint(0, 4) for _ in range(10)]
    sorted_arr = sorted(random_arr)
    assert bucketsort(random_arr, 5) == sorted_arr

    # Тестирование элементов, выходящих за пределы диапазона [0, k-1]
    try:
        bucketsort([5, 6, 7], 5)
    except AssertionError as e:
        assert str(e) == "Элемент массива не входит в диапазон [0, k-1]"


if __name__ == "__main__":
    test_bucketsort()
    print("Все тесты пройдены успешно!")
