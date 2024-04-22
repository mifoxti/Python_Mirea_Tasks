class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def stall(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'G'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'A'
            return 6
        elif self.state == 'G':
            self.state = 'D'
            return 11
        else:
            raise MealyError("stall")

    def trim(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'G':
            self.state = 'A'
            return 10
        else:
            raise MealyError("trim")

    def patch(self):
        if self.state == 'B':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 9
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
    raises(lambda: automaton.patch(), MealyError)
    raises(lambda: automaton.trim(), MealyError)
    assert automaton.state == 'A'
    assert automaton.stall() == 0
    assert automaton.state == 'B'
    assert automaton.stall() == 2
    assert automaton.state == 'G'
    assert automaton.trim() == 10  # A
    assert automaton.stall() == 0  # B
    assert automaton.trim() == 1
    assert automaton.state == 'C'
    raises(lambda: automaton.patch(), MealyError)
    raises(lambda: automaton.trim(), MealyError)
    assert automaton.stall() == 4
    assert automaton.state == 'D'
    raises(lambda: automaton.patch(), MealyError)
    assert automaton.trim() == 5
    assert automaton.state == 'E'
    raises(lambda: automaton.trim(), MealyError)
    raises(lambda: automaton.stall(), MealyError)
    assert automaton.patch() == 7
    assert automaton.state == 'F'
    raises(lambda: automaton.trim(), MealyError)
    raises(lambda: automaton.stall(), MealyError)
    assert automaton.patch() == 8
    assert automaton.stall() == 11
    assert automaton.stall() == 6
    assert automaton.stall() == 0
    assert automaton.patch() == 3
    assert automaton.trim() == 5
    assert automaton.patch() == 7
    assert automaton.patch() == 8
    assert automaton.patch() == 9
    raises(lambda: automaton.trim(), MealyError)
    raises(lambda: automaton.stall(), MealyError)
    raises(lambda: automaton.patch(), MealyError)
    assert automaton.state == 'H'
    automaton = MealyAutomaton()
    assert automaton.stall() == 0
    assert automaton.stall() == 2
    assert automaton.patch() == 9
    automaton = MealyAutomaton()
    assert automaton.stall() == 0
    assert automaton.stall() == 2
    assert automaton.patch() == 9

