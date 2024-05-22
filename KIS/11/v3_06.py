class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def load(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'C':
            self.state = 'A'
            return 4
        elif self.state == 'D':
            self.state = 'A'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'G':
            self.state = 'A'
            return 9
        else:
            raise MealyError("load")

    def patch(self):
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
            return 5
        elif self.state == 'F':
            self.state = 'G'
            return 8
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
    assert automaton.load() == 1
    assert automaton.patch() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.load(), MealyError)
    assert automaton.patch() == 2
    assert automaton.state == 'C'
    assert automaton.load() == 4
    automaton.state = 'C'
    assert automaton.patch() == 3
    assert automaton.state == 'D'
    assert automaton.load() == 6
    automaton.state = 'D'
    assert automaton.patch() == 5
    assert automaton.state == 'E'
    raises(lambda: automaton.patch(), MealyError)
    assert automaton.load() == 7
    assert automaton.state == 'F'
    assert automaton.patch() == 8
    assert automaton.state == 'G'
    assert automaton.load() == 9
