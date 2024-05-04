class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def paint(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'C'
            return 8
        else:
            raise MealyError("paint")

    def show(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'D'
            return 5
        elif self.state == 'F':
            self.state = 'D'
            return 7
        else:
            raise MealyError("show")


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
    assert o.paint() == 1
    assert o.show() == 0
    assert o.state == 'B'
    raises(lambda: o.paint(), MealyError)
    assert o.show() == 2
    assert o.state == 'C'
    raises(lambda: o.paint(), MealyError)
    assert o.show() == 3
    assert o.state == 'D'
    assert o.show() == 5
    assert o.paint() == 4
    assert o.state == 'E'
    raises(lambda: o.show(), MealyError)
    assert o.paint() == 6
    assert o.state == 'F'
    assert o.show() == 7
    assert o.paint() == 4
    assert o.paint() == 6
    assert o.paint() == 8
