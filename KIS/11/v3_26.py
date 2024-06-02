class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def crash(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'A'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'F':
            self.state = 'C'
            return 8
        else:
            raise MealyError("crash")

    def stash(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'E':
            self.state = 'F'
            return 5
        else:
            raise MealyError("stash")

    def sit(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'F':
            self.state = 'F'
            return 7
        elif self.state == 'E':
            self.state = 'A'
            return 6
        else:
            raise MealyError("sit")


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
    raises(lambda: automaton.stash(), MealyError)
    raises(lambda: automaton.sit(), MealyError)
    assert automaton.crash() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.crash(), MealyError)
    assert automaton.stash() == 1
    assert automaton.state == 'C'
    assert automaton.crash() == 3
    automaton.state = 'C'
    assert automaton.sit() == 2
    assert automaton.state == 'D'
    assert automaton.crash() == 4
    assert automaton.state == 'E'
    assert automaton.sit() == 6
    automaton.state = 'E'
    assert automaton.stash() == 5
    assert automaton.state == 'F'
    assert automaton.sit() == 7
    assert automaton.crash() == 8
