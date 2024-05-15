class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def open(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'F'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'C'
            return 6
        elif self.state == 'F':
            self.state = 'F'
            return 9
        elif self.state == 'G':
            self.state = 'D'
            return 11
        else:
            raise MealyError("open")

    def dash(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 5
        elif self.state == 'F':
            self.state = 'C'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise MealyError("dash")

    def begin(self):
        if self.state == 'F':
            self.state = 'G'
            return 7
        else:
            raise MealyError("begin")


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
    automaton = main()
    assert automaton.state == 'A'
    assert automaton.open() == 0
    assert automaton.state == 'B'
    assert automaton.dash() == 1
    assert automaton.state == 'C'
    assert automaton.dash() == 3
    assert automaton.state == 'D'
    assert automaton.open() == 4
    assert automaton.state == 'E'
    assert automaton.open() == 6
    assert automaton.dash() == 3
    assert automaton.open() == 4
    assert automaton.dash() == 5
    assert automaton.state == 'F'
    assert automaton.open() == 9
    assert automaton.dash() == 8
    assert automaton.dash() == 3
    assert automaton.open() == 4
    assert automaton.dash() == 5
    assert automaton.begin() == 7
    assert automaton.state == 'G'
    assert automaton.open() == 11
    assert automaton.open() == 4
    assert automaton.dash() == 5
    assert automaton.begin() == 7
    assert automaton.dash() == 10
    assert automaton.state == 'H'
    raises(lambda: automaton.open(), MealyError)
    raises(lambda: automaton.dash(), MealyError)
    raises(lambda: automaton.open(), MealyError)
    raises(lambda: automaton.begin(), MealyError)
    automaton = main()
    automaton.state = 'B'
    assert automaton.open() == 2
