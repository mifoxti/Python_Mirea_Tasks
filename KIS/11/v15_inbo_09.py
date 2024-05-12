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
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("step")

    def smash(self):
        if self.state == 'A':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 6
        else:
            raise MealyError("smash")

    def shade(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        elif self.state == 'C':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'A'
            return 9
        else:
            raise MealyError("shade")


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
    raises(lambda: automaton.smash(), MealyError)
    raises(lambda: automaton.shade(), MealyError)
    assert automaton.step() == 3
    assert automaton.state == 'C'
    raises(lambda: automaton.step(), MealyError)
    assert automaton.smash() == 4
    assert automaton.state == 'D'
    assert automaton.smash() == 6
    assert automaton.state == 'E'
    assert automaton.step() == 7
    assert automaton.state == 'F'
    assert automaton.shade() == 9
    assert automaton.smash() == 2
    assert automaton.shade() == 5
    automaton = main()
    assert automaton.shade() == 1
    assert automaton.step() == 7
    assert automaton.step() == 8
    assert automaton.state == 'G'
