class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def step(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            self.state = 'D'
            return 8

    def mask(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        elif self.state == 'B':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'D'
            return 6
        else:
            raise MealyError("mask")


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
    assert automaton.step() == 0
    assert automaton.state == 'B'
    assert automaton.step() == 2
    assert automaton.state == 'C'
    raises(lambda: automaton.mask(), MealyError)
    assert automaton.step() == 4
    assert automaton.state == 'D'
    assert automaton.mask() == 6
    assert automaton.step() == 5
    raises(lambda: automaton.mask(), MealyError)
    assert automaton.state == 'E'
    assert automaton.step() == 7
    assert automaton.state == 'F'
    raises(lambda: automaton.mask(), MealyError)
    assert automaton.step() == 8
    automaton = main()
    assert automaton.mask() == 1
    automaton = main()
    assert automaton.step() == 0
    assert automaton.mask() == 3
