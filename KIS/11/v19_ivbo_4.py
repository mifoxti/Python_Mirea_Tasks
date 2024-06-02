class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def visit(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'A'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError("visit")

    def trim(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'B':
            self.state = 'D'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'E':
            self.state = 'E'
            return 8
        else:
            raise MealyError("trim")


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
    assert automaton.visit() == 0
    assert automaton.state == 'B'
    assert automaton.visit() == 2
    assert automaton.state == 'C'
    assert automaton.visit() == 5
    automaton.state = 'B'
    assert automaton.trim() == 3
    assert automaton.state == 'D'
    automaton.state = 'C'
    assert automaton.trim() == 4
    automaton.state = 'A'
    assert automaton.trim() == 1
    assert automaton.visit() == 6
    assert automaton.state == 'E'
    assert automaton.trim() == 8
    assert automaton.visit() == 7
    assert automaton.state == 'F'
    raises(lambda: automaton.trim(), MealyError)
    raises(lambda: automaton.visit(), MealyError)
