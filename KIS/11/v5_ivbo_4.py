class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def step(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'F':
            self.state = 'F'
            return 8
        elif self.state == 'E':
            self.state = 'F'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'C':
            self.state = 'D'
            return 3
        else:
            raise MealyError('step')

    def scale(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'E':
            self.state = 'C'
            return 6
        elif self.state == 'F':
            self.state = 'D'
            return 7
        else:
            raise MealyError("scale")


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
    assert automaton.scale() == 2
    assert automaton.state == 'C'
    automaton.state = 'A'
    assert automaton.scale() == 1
    assert automaton.step() == 3
    assert automaton.state == 'D'
    assert automaton.step() == 4
    assert automaton.state == 'E'
    assert automaton.scale() == 6
    automaton.state = 'E'
    assert automaton.step() == 5
    assert automaton.state == 'F'
    assert automaton.step() == 8
    assert automaton.scale() == 7
    automaton.state = 'none'
    raises(lambda: automaton.step(), MealyError)
    raises(lambda: automaton.scale(), MealyError)
