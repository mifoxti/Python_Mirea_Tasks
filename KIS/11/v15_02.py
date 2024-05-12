class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def chalk(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'D'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 5
        elif self.state == 'F':
            self.state = 'F'
            return 7
        else:
            raise MealyError("chalk")

    def mix(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 3
        elif self.state == 'E':
            self.state = 'B'
            return 6
        elif self.state == 'F':
            self.state = 'C'
            return 8
        else:
            raise MealyError("mix")


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
    raises(lambda: automaton.mix(), MealyError)
    assert automaton.chalk() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.chalk(), MealyError)
    assert automaton.mix() == 1
    assert automaton.state == 'C'
    assert automaton.mix() == 2
    assert automaton.state == 'D'
    assert automaton.chalk() == 4
    assert automaton.mix() == 3
    assert automaton.state == 'E'
    assert automaton.mix() == 6
    assert automaton.mix() == 1
    assert automaton.mix() == 2
    assert automaton.mix() == 3
    assert automaton.chalk() == 5
    assert automaton.state == 'F'
    assert automaton.chalk() == 7
    assert automaton.mix() == 8
