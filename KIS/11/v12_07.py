class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def crack(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'C':
            self.state = 'A'
            return 4
        elif self.state == 'E':
            self.state = 'A'
            return 8
        else:
            raise MealyError("crack")

    def coat(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("coat")

    def apply(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'G'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError("apply")

    def cut(self):
        if self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'C'
            return 10
        elif self.state == 'G':
            self.state = 'H'
            return 11
        else:
            raise MealyError("cut")


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
    assert automaton.crack() == 1
    assert automaton.coat() == 0
    assert automaton.state == 'B'
    assert automaton.coat() == 2
    assert automaton.state == 'C'
    assert automaton.crack() == 4
    automaton.state = 'C'
    assert automaton.apply() == 3
    assert automaton.state == 'D'
    assert automaton.apply() == 6
    assert automaton.state == 'G'
    automaton.state = 'D'
    assert automaton.cut() == 5
    assert automaton.state == 'E'
    assert automaton.crack() == 8
    automaton.state = 'E'
    assert automaton.apply() == 7
    assert automaton.state == 'F'
    assert automaton.cut() == 10
    automaton.state = 'F'
    assert automaton.coat() == 9
    assert automaton.state == 'G'
    assert automaton.cut() == 11
    raises(lambda: automaton.coat(), MealyError)
    raises(lambda: automaton.cut(), MealyError)
    raises(lambda: automaton.apply(), MealyError)
    raises(lambda: automaton.crack(), MealyError)
