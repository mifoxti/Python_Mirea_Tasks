class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def reset(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'D'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'C'
            return 6
        elif self.state == 'F':
            self.state = 'C'
            return 7
        else:
            raise MealyError("reset")

    def spawn(self):
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
            self.state = 'F'
            return 8
        else:
            raise MealyError("spawn")


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
    raises(lambda: automaton.spawn(), MealyError)
    assert automaton.reset() == 0
    assert automaton.state == 'B'
    assert automaton.spawn() == 1
    assert automaton.state == 'C'
    raises(lambda: automaton.reset(), MealyError)
    assert automaton.spawn() == 3
    assert automaton.state == 'D'
    automaton.state = 'B'
    assert automaton.reset() == 2
    assert automaton.reset() == 4
    assert automaton.state == 'E'
    assert automaton.reset() == 6
    automaton.state = 'E'
    assert automaton.spawn() == 5
    assert automaton.state == 'F'
    assert automaton.spawn() == 8
    assert automaton.reset() == 7
