class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def punch(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("punch")

    def trace(self):
        if self.state == 'B':
            self.state = 'E'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 6
        else:
            raise MealyError("trace")

    def smash(self):
        if self.state == 'B':
            self.state = 'G'
            return 3
        elif self.state == 'C':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'E'
            return 8
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
    assert automaton.state == 'A'
    assert automaton.punch() == 0
    assert automaton.state == 'B'
    assert automaton.punch() == 1
    assert automaton.state == 'C'
    assert automaton.punch() == 4
    assert automaton.state == 'D'
    assert automaton.trace() == 6
    assert automaton.state == 'E'
    assert automaton.smash() == 8
    automaton.state = 'C'
    assert automaton.smash() == 5
    automaton.state = 'B'
    assert automaton.smash() == 3
    automaton.state = 'B'
    assert automaton.trace() == 2
    assert automaton.punch() == 7
    assert automaton.state == 'F'
    assert automaton.punch() == 9
    assert automaton.state == 'G'
    raises(lambda: automaton.trace(), MealyError)
    raises(lambda: automaton.punch(), MealyError)
    raises(lambda: automaton.smash(), MealyError)
