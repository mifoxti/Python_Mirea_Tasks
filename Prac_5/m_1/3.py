class raises:
    def __init__(self, expected_exception):
        self.expected_exception = expected_exception
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            raise AssertionError(f"{self.expected_exception.__name__} �� ���� ����������")
        if not issubclass(exc_type, self.expected_exception):
            # ���������� ������ ����������
            return False
        self.exception = exc_value
        return True


# ������ �������������:
class MealyError(Exception):
    pass


def some_function():
    raise MealyError("������ � �������")


# ���������, ��� ���������� MealyError ���� ����������
with raises(MealyError) as e:
    some_function()

# ��������� ������ � ����������
assert isinstance(e.exception, MealyError)
print("���� ������� �������!")
