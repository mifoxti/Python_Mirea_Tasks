class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def scan(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'B'
            return 2
        elif self.state == 'E':
            self.state = 'A'
            return 8
        else:
            raise MealyError("scan")

    def sort(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'E'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'E'
            return 7
        else:
            raise MealyError("sort")

    def speed(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise MealyError("speed")


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
    assert automaton.scan() == 0
    assert automaton.state == 'B'
    assert automaton.scan() == 2
    assert automaton.sort() == 1
    assert automaton.state == 'C'
    assert automaton.speed() == 3
    assert automaton.state == 'D'
    assert automaton.sort() == 5
    automaton.state = 'C'
    assert automaton.sort() == 4
    assert automaton.state == 'E'
    assert automaton.sort() == 7
    assert automaton.scan() == 8
    automaton.state = 'E'
    assert automaton.speed() == 6
    assert automaton.state == 'F'
    raises(lambda: automaton.speed(), MealyError)
    raises(lambda: automaton.sort(), MealyError)
    raises(lambda: automaton.scan(), MealyError)
