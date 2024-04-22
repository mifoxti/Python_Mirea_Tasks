class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def melt(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 3
        elif self.state == 'E':
            self.state = 'G'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 7
        else:
            self.state = 'A'
            return 9

    def cast(self):
        if self.state == 'D':
            self.state = 'G'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 5
        elif self.state == 'F':
            self.state = 'B'
            return 8
        else:
            raise MealyError("cast")


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
    raises(lambda: automaton.cast(), MealyError)
    assert automaton.melt() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.cast(), MealyError)
    assert automaton.melt() == 1
    assert automaton.state == 'C'
    raises(lambda: automaton.cast(), MealyError)
    assert automaton.melt() == 2
    assert automaton.state == 'D'
    assert automaton.melt() == 3
    assert automaton.state == 'E'
    assert automaton.melt() == 6
    assert automaton.state == 'G'
    raises(lambda: automaton.cast(), MealyError)
    assert automaton.melt() == 9
    assert automaton.melt() == 0
    assert automaton.melt() == 1
    assert automaton.melt() == 2
    assert automaton.cast() == 4
    assert automaton.melt() == 9
    assert automaton.melt() == 0
    assert automaton.melt() == 1
    assert automaton.melt() == 2
    assert automaton.melt() == 3
    assert automaton.cast() == 5
    assert automaton.state == 'F'
    assert automaton.cast() == 8
    automaton = main()
    assert automaton.melt() == 0
    assert automaton.melt() == 1
    assert automaton.melt() == 2
    assert automaton.melt() == 3
    assert automaton.cast() == 5
    assert automaton.melt() == 7
    assert automaton.melt() == 9
