class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def color(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'B'
            return 3
        elif self.state == 'D':
            self.state = 'B'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError("color")

    def lower(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'F'
            return 8
        elif self.state == 'A':
            self.state = 'D'
            return 1
        else:
            raise MealyError("lower")


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
    assert automaton.color() == 0
    assert automaton.state == 'B'
    assert automaton.color() == 3
    assert automaton.lower() == 2
    assert automaton.state == 'C'
    raises(lambda: automaton.color(), MealyError)
    assert automaton.lower() == 4
    assert automaton.state == 'D'
    assert automaton.color() == 6
    automaton.state = 'A'
    assert automaton.lower() == 1
    assert automaton.lower() == 5
    assert automaton.state == 'E'
    raises(lambda: automaton.lower(), MealyError)
    assert automaton.color() == 7
    assert automaton.state == 'F'
    assert automaton.lower() == 8
