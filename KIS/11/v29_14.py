class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def herd(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'E'
            return 8
        else:
            raise MealyError("herd")

    def trash(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'E':
            self.state = 'A'
            return 7
        else:
            raise MealyError("trash")

    def hurry(self):
        if self.state == 'C':
            self.state = 'E'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("hurry")


def main():
    return MealyAutomaton()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
        assert output is None


def test():
    o = main()
    assert o.state == 'A'
    raises(lambda: o.hurry(), MealyError)
    assert o.herd() == 1
    assert o.trash() == 0
    assert o.state == 'B'
    raises(lambda: o.trash(), MealyError)
    assert o.herd() == 2
    assert o.state == 'C'
    assert o.herd() == 3
    assert o.state == 'D'
    raises(lambda: o.herd(), MealyError)
    assert o.hurry() == 5
    assert o.state == 'E'
    assert o.herd() == 8
    assert o.trash() == 7
    assert o.trash() == 0
    assert o.herd() == 2
    assert o.hurry() == 4
    assert o.hurry() == 6
    assert o.state == 'F'
    assert o.hurry() == 9
    assert o.state == 'G'
