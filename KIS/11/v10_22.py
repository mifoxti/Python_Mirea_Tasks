class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def rev(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise MealyError("rev")

    def stash(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise MealyError("stash")

    def hurry(self):
        if self.state == 'A':
            self.state = 'E'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'A'
            return 6
        else:
            raise MealyError("hurry")


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
    assert automaton.stash() == 1
    assert automaton.hurry() == 2
    automaton.state = 'A'
    assert automaton.rev() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.rev(), MealyError)
    raises(lambda: automaton.hurry(), MealyError)
    assert automaton.stash() == 3
    assert automaton.state == 'C'
    assert automaton.hurry() == 4
    assert automaton.state == 'D'
    raises(lambda: automaton.stash(), MealyError)
    assert automaton.hurry() == 6
    automaton.state = 'D'
    assert automaton.rev() == 5
    assert automaton.state == 'E'
    assert automaton.stash() == 7
    assert automaton.state == 'F'
    assert automaton.stash() == 8
