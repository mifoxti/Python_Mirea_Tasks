class raises:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            raise AssertionError(f"{self.exception.__name__} was not raised")
        if not issubclass(exc_type, self.exception):
            raise AssertionError(f"Expected {self.exception.__name__}, but got {exc_type.__name__}")
        return True

class MealyError(Exception):
    pass

def divide(x, y):
    """
    Divide two numbers.

    Parameters:
    x (int): The numerator.
    y (int): The denominator.

    Raises:
    MealyError: If the denominator is zero.

    Returns:
    float: The result of the division.

    Examples:
    >>> divide(10, 2)
    5.0
    >>> divide(10, 0)
    Traceback (most recent call last):
        ...
    MealyError: Division by zero is not allowed
    >>> divide(0, 5)
    0.0
    """
    if y == 0:
        raise MealyError("Division by zero is not allowed")
    return x / y

import doctest

if __name__ == "__main__":
    doctest.testmod()