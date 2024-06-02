class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def debug(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'A'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'A'
            return 8
        else:
            raise MealyError("debug")

    def amble(self):
        if self.state == 'A':
            self.state = 'F'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'B'
            return 7
        else:
            raise MealyError("amble")

    def patch(self):
        if self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise MealyError("patch")


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
    assert automaton.debug() == 0
    assert automaton.state == 'B'
    assert automaton.debug() == 2
    assert automaton.state == 'C'
    assert automaton.debug() == 4
    automaton.state = 'C'
    assert automaton.amble() == 3
    assert automaton.state == 'D'
    assert automaton.debug() == 5
    assert automaton.state == 'E'
    assert automaton.debug() == 8
    automaton.state = 'E'
    assert automaton.amble() == 7
    automaton.state = 'E'
    assert automaton.patch() == 6
    assert automaton.state == 'F'
    automaton.state = 'A'
    assert automaton.amble() == 1
    raises(lambda: automaton.amble(), MealyError)
    raises(lambda: automaton.debug(), MealyError)
    raises(lambda: automaton.patch(), MealyError)
