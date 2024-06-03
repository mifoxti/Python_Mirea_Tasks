class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def cut(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'E'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'C':
            self.state = 'C'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("cut")

    def align(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'F':
            self.state = 'D'
            return 9
        else:
            raise MealyError("align")


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
    assert automaton.cut() == 0
    assert automaton.state == 'B'
    assert automaton.align() == 2
    assert automaton.state == 'C'
    assert automaton.cut() == 5
    automaton.state = 'A'
    assert automaton.align() == 1
    assert automaton.align() == 4
    assert automaton.state == 'D'
    assert automaton.cut() == 6
    assert automaton.state == 'E'
    assert automaton.cut() == 7
    assert automaton.state == 'F'
    assert automaton.align() == 9
    automaton.state = 'B'
    assert automaton.cut() == 3
    automaton.state = 'F'
    assert automaton.cut() == 8
    assert automaton.state == 'G'
    raises(lambda: automaton.align(), MealyError)
    raises(lambda: automaton.cut(), MealyError)
