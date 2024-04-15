class raises:
    def __init__(self, expected_exception):
        self.expected_exception = expected_exception
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            raise AssertionError(f"{self.expected_exception.__name__} не было возбуждено")
        if not issubclass(exc_type, self.expected_exception):
            # Пропускаем другие исключения
            return False
        self.exception = exc_value
        return True


# Пример использования:
class MealyError(Exception):
    pass


def some_function():
    raise MealyError("Ошибка в функции")


# Проверяем, что исключение MealyError было возбуждено
with raises(MealyError) as e:
    some_function()

# Проверяем доступ к исключению
assert isinstance(e.exception, MealyError)
print("Тест пройден успешно!")
