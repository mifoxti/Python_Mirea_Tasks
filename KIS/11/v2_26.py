class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def hoard(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'F'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise MealyError('hoard')

    def race(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'A'
            return 4
        elif self.state == 'E':
            self.state = 'B'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("race")

    def tail(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'G':
            self.state = 'G'
            return 9
        else:
            raise MealyError("tail")


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
    assert automaton.hoard() == 0
    assert automaton.state == 'B'
    assert automaton.race() == 1
    assert automaton.state == 'C'
    assert automaton.race() == 4
    automaton.state = 'C'
    assert automaton.tail() == 2
    assert automaton.state == 'D'
    assert automaton.hoard() == 5
    assert automaton.state == 'E'
    assert automaton.hoard() == 6
    assert automaton.state == 'F'
    assert automaton.race() == 8
    assert automaton.state == 'G'
    assert automaton.tail() == 9
    automaton.state = 'C'
    assert automaton.hoard() == 3
    automaton.state = 'E'
    assert automaton.race() == 7
    automaton.state = 'None'
    raises(lambda: automaton.hoard(), MealyError)
    raises(lambda: automaton.race(), MealyError)
    raises(lambda: automaton.tail(), MealyError)
