class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def race(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'A'
            return 9
        elif self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise MealyError("race")

    def forge(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'B'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("forge")


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
    assert automaton.race() == 1
    assert automaton.forge() == 0
    assert automaton.state == 'B'
    assert automaton.race() == 2
    assert automaton.state == 'C'
    assert automaton.forge() == 3
    assert automaton.state == 'D'
    assert automaton.forge() == 6
    automaton.state = 'D'
    assert automaton.race() == 5
    automaton.state = 'C'
    assert automaton.race() == 4
    assert automaton.state == 'E'
    assert automaton.race() == 7
    assert automaton.state == 'F'
    assert automaton.race() == 9
    automaton.state = 'F'
    assert automaton.forge() == 8
    assert automaton.state == 'G'
    raises(lambda: automaton.race(), MealyError)
    raises(lambda: automaton.forge(), MealyError)
