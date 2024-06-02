class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def hop(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'E'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise MealyError("hop")

    def visit(self):
        if self.state == 'A':
            self.state = 'H'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'A'
            return 9
        elif self.state == 'H':
            self.state = 'D'
            return 11
        else:
            raise MealyError("visit")


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
    assert automaton.hop() == 0
    assert automaton.state == 'B'
    assert automaton.visit() == 2
    assert automaton.state == 'C'
    assert automaton.hop() == 4
    assert automaton.state == 'D'
    assert automaton.hop() == 6
    assert automaton.state == 'E'
    automaton.state = 'B'
    assert automaton.hop() == 3
    automaton.state = 'C'
    assert automaton.visit() == 5
    assert automaton.visit() == 7
    assert automaton.state == 'F'
    assert automaton.visit() == 9
    assert automaton.visit() == 1
    assert automaton.state == 'H'
    assert automaton.visit() == 11
    automaton.state = 'F'
    assert automaton.hop() == 8
    assert automaton.state == 'G'
    assert automaton.hop() == 10
    automaton.state = 'None'
    raises(lambda: automaton.visit(), MealyError)
    raises(lambda: automaton.hop(), MealyError)
