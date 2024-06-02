class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def rush(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError('rush')

    def chalk(self):
        if self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'A':
            self.state = 'D'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise MealyError("chalk")

    def bolt(self):
        if self.state == 'A':
            self.state = 'G'
            return 1
        elif self.state == 'C':
            self.state = 'A'
            return 5
        elif self.state == 'F':
            self.state = 'D'
            return 9
        elif self.state == 'G':
            self.state = 'D'
            return 11
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
    assert automaton.rush() == 0
    assert automaton.state == 'B'
    assert automaton.chalk() == 3
    assert automaton.state == 'C'
    assert automaton.bolt() == 5
    assert automaton.chalk() == 2
    assert automaton.state == 'D'
    automaton.state = 'C'
    assert automaton.chalk() == 4
    assert automaton.state == 'D'
    assert automaton.rush() == 6
    assert automaton.state == 'E'
    assert automaton.rush() == 7
    assert automaton.state == 'F'
    assert automaton.bolt() == 9
    automaton.state = 'F'
    assert automaton.chalk() == 8
    assert automaton.state == 'G'
    assert automaton.bolt() == 11
    automaton.state = 'G'
    assert automaton.chalk() == 10
    assert automaton.state == 'H'
    automaton.state = 'A'
    assert automaton.bolt() == 1
    assert automaton.chalk() == 10
    raises(lambda: automaton.chalk(), MealyError)
    raises(lambda: automaton.rush(), MealyError)
    raises(lambda: automaton.bolt(), MealyError)
