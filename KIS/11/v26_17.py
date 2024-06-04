class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def rush(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 7
        elif self.state == 'G':
            self.state = 'C'
            return 9
        else:
            raise MealyError("rush")

    def apply(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'E'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'G':
            self.state = 'D'
            return 8
        else:
            raise MealyError("apply")


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
    assert automaton.rush() == 1
    assert automaton.apply() == 0
    assert automaton.state == 'B'
    assert automaton.rush() == 2
    assert automaton.state == 'C'
    assert automaton.apply() == 4
    assert automaton.state == 'D'
    assert automaton.apply() == 5
    assert automaton.state == 'E'
    automaton.state = 'B'
    assert automaton.apply() == 3
    assert automaton.rush() == 6
    assert automaton.state == 'F'
    assert automaton.rush() == 7
    assert automaton.state == 'G'
    assert automaton.apply() == 8
    automaton.state = 'G'
    assert automaton.rush() == 9
    automaton.state = 'None'
    raises(lambda: automaton.apply(), MealyError)
    raises(lambda: automaton.rush(), MealyError)
