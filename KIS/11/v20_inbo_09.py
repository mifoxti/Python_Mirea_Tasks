class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def scale(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
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
        elif self.state == 'F':
            self.state = 'F'
            return 9
        else:
            raise MealyError("scale")

    def reset(self):
        if self.state == 'A':
            self.state = 'F'
            return 1
        elif self.state == 'D':
            self.state = 'F'
            return 5
        elif self.state == 'E':
            self.state = 'C'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 10
        elif self.state == 'H':
            self.state = 'A'
            return 11
        else:
            raise MealyError("reset")


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
    assert automaton.scale() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.reset(), MealyError)
    assert automaton.scale() == 2
    assert automaton.state == 'C'
    assert automaton.scale() == 3
    assert automaton.state == 'D'
    assert automaton.scale() == 4
    assert automaton.state == 'E'
    assert automaton.reset() == 7
    assert automaton.state == 'C'
    automaton.state = 'D'
    assert automaton.reset() == 5
    assert automaton.state == 'F'
    automaton.state = 'E'
    assert automaton.scale() == 6
    assert automaton.scale() == 9
    assert automaton.reset() == 8
    assert automaton.state == 'G'
    raises(lambda: automaton.scale(), MealyError)
    assert automaton.reset() == 10
    assert automaton.state == 'H'
    assert automaton.reset() == 11
    assert automaton.reset() == 1
