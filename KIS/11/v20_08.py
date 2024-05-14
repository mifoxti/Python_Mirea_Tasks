class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def fill(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'A'
            return 5
        elif self.state == 'E':
            self.state = 'C'
            return 7
        else:
            raise MealyError("fill")

    def open(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            self.state = 'F'
            return 8


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
    assert automaton.fill() == 0
    raises(lambda: automaton.fill(), MealyError)
    assert automaton.state == 'B'
    assert automaton.open() == 2
    assert automaton.state == 'C'
    assert automaton.open() == 3
    assert automaton.state == 'D'
    assert automaton.fill() == 5
    assert automaton.open() == 1
    assert automaton.open() == 3
    assert automaton.open() == 4
    assert automaton.state == 'E'
    assert automaton.fill() == 7
    assert automaton.open() == 3
    assert automaton.open() == 4
    assert automaton.open() == 6
    assert automaton.state == 'F'
    assert automaton.open() == 8
