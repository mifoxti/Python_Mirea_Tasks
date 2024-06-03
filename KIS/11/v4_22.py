class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def swap(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'A'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError('swap')

    def slog(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'D':
            self.state = 'B'
            return 6
        elif self.state == 'F':
            self.state = 'F'
            return 8
        else:
            raise MealyError("slog")


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
    assert automaton.swap() == 0
    assert automaton.state == 'B'
    assert automaton.slog() == 2
    assert automaton.state == 'C'
    assert automaton.swap() == 4
    assert automaton.slog() == 1
    assert automaton.state == 'D'
    assert automaton.slog() == 6
    assert automaton.slog() == 2
    assert automaton.slog() == 3
    assert automaton.swap() == 5
    assert automaton.state == 'E'
    assert automaton.swap() == 7
    assert automaton.state == 'F'
    assert automaton.slog() == 8
    automaton.state = 'None'
    raises(lambda: automaton.swap(), MealyError)
    raises(lambda: automaton.slog(), MealyError)
