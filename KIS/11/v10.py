class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def speed(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'B'
            return 6
        else:
            raise MealyError('speed')

    def slip(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 9
        elif self.state == 'H':
            self.state = 'H'
            return 11
        else:
            raise MealyError("slip")

    def group(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'H':
            self.state = 'F'
            return 10
        else:
            raise MealyError("group")


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
    assert automaton.speed() == 0
    assert automaton.state == 'B'
    assert automaton.slip() == 2
    automaton.state = 'A'
    assert automaton.group() == 1
    assert automaton.state == 'C'
    assert automaton.group() == 3
    assert automaton.speed() == 6
    automaton.state = 'D'
    assert automaton.state == 'D'
    assert automaton.group() == 5
    automaton.state = 'C'
    assert automaton.slip() == 4
    assert automaton.state == 'E'
    assert automaton.slip() == 7
    assert automaton.state == 'F'
    assert automaton.slip() == 8
    assert automaton.state == 'G'
    assert automaton.slip() == 9
    assert automaton.state == 'H'
    assert automaton.slip() == 11
    assert automaton.group() == 10
    automaton.state = 'None'
    raises(lambda: automaton.speed(), MealyError)
    raises(lambda: automaton.group(), MealyError)
    raises(lambda: automaton.slip(), MealyError)
