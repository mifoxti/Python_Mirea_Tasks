class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def make(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'G'
            return 4
        elif self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'G'
            return 11
        else:
            raise MealyError

    def view(self):
        if self.state == 'A':
            self.state = 'F'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'G':
            self.state = 'E'
            return 10
        else:
            raise MealyError("view")

    def trash(self):
        if self.state == 'B':
            self.state = 'E'
            return 3
        elif self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise MealyError('trash')


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
    raises(lambda: automaton.trash(), MealyError)
    assert automaton.make() == 0
    assert automaton.state == 'B'
    assert automaton.view() == 2
    assert automaton.state == 'C'
    assert automaton.make() == 5
    assert automaton.state == 'D'
    assert automaton.make() == 6
    assert automaton.state == 'E'
    assert automaton.make() == 7
    assert automaton.state == 'F'
    assert automaton.make() == 8
    assert automaton.state == 'G'
    assert automaton.make() == 11
    assert automaton.view() == 10
    assert automaton.make() == 7
    assert automaton.make() == 8
    assert automaton.trash() == 9
    assert automaton.state == 'H'
    raises(lambda: automaton.view(), MealyError)
    raises(lambda: automaton.make(), MealyError)
    automaton = main()
    assert automaton.make() == 0
    assert automaton.make() == 4
    automaton = main()
    assert automaton.make() == 0
    assert automaton.trash() == 3
    automaton = main()
    assert automaton.view() == 1
