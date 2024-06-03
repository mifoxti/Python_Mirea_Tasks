class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def tread(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'E':
            self.state = 'F'
            return 8
        elif self.state == 'C':
            self.state = 'F'
            return 4
        else:
            raise MealyError('tread')

    def blame(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'B'
            return 7
        else:
            raise MealyError("blame")

    def carve(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'A'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 6
        else:
            raise MealyError("carve")


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
    assert automaton.blame() == 1
    assert automaton.tread() == 0
    assert automaton.state == 'B'
    assert automaton.carve() == 2
    assert automaton.state == 'C'
    assert automaton.carve() == 5
    automaton.state = 'C'
    assert automaton.blame() == 3
    assert automaton.state == 'D'
    assert automaton.blame() == 7
    automaton.state = 'D'
    assert automaton.carve() == 6
    assert automaton.state == 'E'
    assert automaton.tread() == 8
    automaton.state = 'C'
    assert automaton.tread() == 4
    raises(lambda: automaton.carve(), MealyError)
    raises(lambda: automaton.blame(), MealyError)
    raises(lambda: automaton.tread(), MealyError)
