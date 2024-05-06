class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def color(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
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
            self.state = 'A'
            return 10
        elif self.state == 'H':
            self.state = 'A'
            return 11
        else:
            raise MealyError("color")

    def step(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'B':
            self.state = 'E'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'C'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise MealyError("step")


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
    assert automaton.color() == 0
    assert automaton.state == 'B'
    assert automaton.color() == 2
    assert automaton.state == 'C'
    raises(lambda: automaton.color(), MealyError)
    assert automaton.step() == 4
    assert automaton.state == 'D'
    raises(lambda: automaton.color(), MealyError)
    assert automaton.step() == 5
    assert automaton.state == 'E'
    raises(lambda: automaton.step(), MealyError)
    assert automaton.color() == 6
    assert automaton.state == 'F'
    assert automaton.color() == 7
    assert automaton.state == 'G'
    assert automaton.step() == 9
    assert automaton.state == 'H'
    raises(lambda: automaton.step(), MealyError)
    assert automaton.color() == 11
    assert automaton.step() == 1
    assert automaton.step() == 4
    assert automaton.step() == 5
    assert automaton.color() == 6
    assert automaton.step() == 8
    automaton = main()
    assert automaton.color() == 0
    assert automaton.step() == 3
    assert automaton.color() == 6
    assert automaton.color() == 7
    assert automaton.color() == 10

