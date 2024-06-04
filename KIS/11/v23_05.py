class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def print(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'F':
            self.state = 'G'
            return 7
        else:
            raise MealyError("print")

    def bolt(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'G'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'B'
            return 8
        elif self.state == 'G':
            self.state = 'A'
            return 9
        else:
            raise MealyError("bolt")


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
    assert automaton.print() == 0
    assert automaton.state == 'B'
    assert automaton.print() == 2
    assert automaton.state == 'C'
    assert automaton.bolt() == 3
    assert automaton.state == 'D'
    automaton.state = 'A'
    assert automaton.bolt() == 1
    assert automaton.print() == 4
    assert automaton.state == 'E'
    assert automaton.bolt() == 6
    assert automaton.state == 'F'
    assert automaton.print() == 7
    assert automaton.state == 'G'
    assert automaton.bolt() == 9
    automaton.state = 'F'
    assert automaton.bolt() == 8
    automaton.state = 'D'
    assert automaton.bolt() == 5
    automaton.state = 'None'
    raises(lambda: automaton.print(), MealyError)
    raises(lambda: automaton.bolt(), MealyError)
