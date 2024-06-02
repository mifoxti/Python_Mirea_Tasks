class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def load(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'B'
            return 8
        else:
            raise MealyError("load")

    def grow(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise MealyError("grow")

    def smash(self):
        if self.state == 'E':
            self.state = 'C'
            return 7
        elif self.state == 'A':
            self.state = 'F'
            return 1
        else:
            raise MealyError("smash")


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
    raises(lambda: automaton.grow(), MealyError)
    assert automaton.state == 'A'
    assert automaton.load() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.smash(), MealyError)
    assert automaton.grow() == 2
    raises(lambda: automaton.load(), MealyError)
    assert automaton.state == 'C'
    assert automaton.grow() == 4
    automaton.state = 'B'
    assert automaton.load() == 3
    assert automaton.state == 'D'
    assert automaton.load() == 5
    assert automaton.state == 'E'
    assert automaton.smash() == 7
    automaton.state = 'E'
    assert automaton.load() == 8
    automaton.state = 'E'
    assert automaton.grow() == 6
    assert automaton.state == 'F'
    automaton.state = 'A'
    assert automaton.smash() == 1
