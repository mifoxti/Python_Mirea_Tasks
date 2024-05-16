class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def forge(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'F'
            return 5
        elif self.state == 'F':
            self.state = 'C'
            return 8
        else:
            raise MealyError("forge")

    def print(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            self.state = 'F'
            return 7


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
    assert automaton.forge() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.forge(), MealyError)
    assert automaton.print() == 2
    assert automaton.state == 'C'
    assert automaton.print() == 3
    automaton.state = 'A'
    assert automaton.print() == 1
    assert automaton.state == 'D'
    assert automaton.print() == 4
    assert automaton.state == 'E'
    assert automaton.print() == 6
    assert automaton.state == 'F'
    assert automaton.print() == 7
    automaton.state = 'D'
    assert automaton.forge() == 5
    assert automaton.forge() == 8
