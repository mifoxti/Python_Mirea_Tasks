class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def chain(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'C':
            self.state = 'E'
            return 6
        elif self.state == 'G':
            self.state = 'H'
            return 11

        else:
            raise MealyError("chain")

    def check(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        else:
            raise MealyError("check")

    def merge(self):
        if self.state == 'C':
            self.state = 'F'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 7
        elif self.state == 'E':
            self.state = 'F'
            return 8
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("merge")

    def clone(self):
        if self.state == 'C':
            self.state = 'H'
            return 4
        elif self.state == 'F':
            self.state = 'D'
            return 10
        else:
            raise MealyError("clone")


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
    assert automaton.chain() == 1
    assert automaton.check() == 0
    assert automaton.state == 'B'
    assert automaton.check() == 2
    assert automaton.state == 'C'
    assert automaton.check() == 3
    assert automaton.state == 'D'
    assert automaton.merge() == 7
    assert automaton.state == 'E'
    assert automaton.merge() == 8
    assert automaton.state == 'F'
    assert automaton.merge() == 9
    assert automaton.state == 'G'
    assert automaton.chain() == 11
    assert automaton.state == 'H'
    automaton.state = 'C'
    assert automaton.chain() == 6
    automaton.state = 'C'
    assert automaton.merge() == 5
    automaton.state = 'C'
    assert automaton.clone() == 4
    automaton.state = 'F'
    assert automaton.clone() == 10
    automaton.state = 'None'
    raises(lambda: automaton.clone(), MealyError)
    raises(lambda: automaton.chain(), MealyError)
    raises(lambda: automaton.check(), MealyError)
    raises(lambda: automaton.merge(), MealyError)
