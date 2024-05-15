class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def clear(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'E':
            self.state = 'A'
            return 6
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise MealyError("clear")

    def spin(self):
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
            self.state = 'F'
            return 5
        elif self.state == 'G':
            self.state = 'B'
            return 11
        else:
            raise MealyError("spin")

    def coast(self):
        if self.state == 'D':
            self.state = 'A'
            return 4
        elif self.state == 'E':
            self.state = 'B'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("coast")

    def pull(self):
        if self.state == 'E':
            self.state = 'E'
            return 8
        else:
            raise MealyError("pull")


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
    assert automaton.clear() == 0
    assert automaton.state == 'B'
    assert automaton.spin() == 1
    assert automaton.state == 'C'
    assert automaton.spin() == 2
    assert automaton.state == 'D'
    assert automaton.spin() == 3
    assert automaton.state == 'E'
    assert automaton.pull() == 8
    assert automaton.coast() == 7
    automaton.state = 'D'
    assert automaton.coast() == 4
    automaton.state = 'E'
    assert automaton.clear() == 6
    automaton.state = 'E'
    assert automaton.spin() == 5
    assert automaton.state == 'F'
    assert automaton.coast() == 9
    assert automaton.state == 'G'
    assert automaton.spin() == 11
    automaton.state = 'G'
    assert automaton.clear() == 10
    assert automaton.state == 'H'
    raises(lambda: automaton.coast(), MealyError)
    raises(lambda: automaton.spin(), MealyError)
    raises(lambda: automaton.clear(), MealyError)
    raises(lambda: automaton.pull(), MealyError)
