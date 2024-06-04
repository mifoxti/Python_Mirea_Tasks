class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def skew(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("skew")

    def tail(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise MealyError("tail")

    def fill(self):
        if self.state == 'A':
            self.state = 'D'
            return 2
        elif self.state == 'D':
            self.state = 'B'
            return 7
        elif self.state == 'E':
            self.state = 'F'
            return 8
        else:
            raise MealyError("fill")


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
    assert automaton.skew() == 0
    assert automaton.state == 'B'
    assert automaton.tail() == 3
    assert automaton.state == 'C'
    assert automaton.tail() == 4
    assert automaton.state == 'D'
    assert automaton.fill() == 7
    automaton.state = 'A'
    assert automaton.tail() == 1
    automaton.state = 'A'
    assert automaton.fill() == 2
    assert automaton.tail() == 5
    assert automaton.state == 'E'
    assert automaton.fill() == 8
    automaton.state = 'D'
    assert automaton.skew() == 6
    assert automaton.state == 'F'
    assert automaton.skew() == 9
    assert automaton.state == 'G'
    raises(lambda: automaton.fill(), MealyError)
    raises(lambda: automaton.tail(), MealyError)
    raises(lambda: automaton.skew(), MealyError)
