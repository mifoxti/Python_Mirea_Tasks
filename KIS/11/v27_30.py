class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def apply(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("apply")

    def lower(self):
        if self.state == 'A':
            self.state = 'H'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'E':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise MealyError("lower")

    def sit(self):
        if self.state == 'A':
            self.state = 'G'
            return 2
        elif self.state == 'B':
            self.state = 'D'
            return 4
        elif self.state == 'G':
            self.state = 'C'
            return 11
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
    assert automaton.apply() == 0
    assert automaton.state == 'B'
    assert automaton.lower() == 3
    assert automaton.state == 'C'
    assert automaton.lower() == 5
    assert automaton.state == 'D'
    assert automaton.apply() == 6
    assert automaton.state == 'E'
    assert automaton.apply() == 7
    assert automaton.state == 'F'
    assert automaton.apply() == 9
    assert automaton.state == 'G'
    assert automaton.sit() == 11
    automaton.state = 'B'
    assert automaton.sit() == 4
    automaton.state = 'E'
    assert automaton.lower() == 8
    assert automaton.lower() == 10
    assert automaton.state == 'H'
    automaton.state = 'A'
    assert automaton.sit() == 2
    automaton.state = 'A'
    assert automaton.lower() == 1
    raises(lambda: automaton.lower(), MealyError)
    raises(lambda: automaton.sit(), MealyError)
    raises(lambda: automaton.apply(), MealyError)
