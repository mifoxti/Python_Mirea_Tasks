class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def trash(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'D'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'B'
            return 8
        else:
            raise MealyError("trash")

    def patch(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'A'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 7
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
    assert automaton.trash() == 0
    assert automaton.state == 'B'
    assert automaton.patch() == 2
    assert automaton.state == 'C'
    assert automaton.trash() == 4
    assert automaton.state == 'D'
    assert automaton.trash() == 6
    assert automaton.state == 'E'
    assert automaton.trash() == 8
    assert automaton.trash() == 3
    automaton.state = 'C'
    assert automaton.patch() == 5
    assert automaton.patch() == 1
    assert automaton.patch() == 7
    assert automaton.state == 'F'
    raises(lambda: automaton.trash(), MealyError)
    raises(lambda: automaton.patch(), MealyError)
