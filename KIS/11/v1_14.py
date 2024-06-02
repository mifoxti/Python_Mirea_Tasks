class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def step(self):
        if self.state == 'E':
            self.state = 'F'
            return 4
        elif self.state == 'F':
            self.state = 'G'
            return 7
        else:
            raise MealyError('step')

    def turn(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'E':
            self.state = 'C'
            return 5
        elif self.state == 'F':
            self.state = 'F'
            return 8
        else:
            raise MealyError("turn")

    def link(self):
        if self.state == 'D':
            self.state = 'E'
            return 3
        elif self.state == 'E':
            self.state = 'A'
            return 6
        elif self.state == 'G':
            self.state = 'C'
            return 9
        else:
            raise MealyError("link")


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
    raises(lambda: automaton.link(), MealyError)
    raises(lambda: automaton.step(), MealyError)
    assert automaton.turn() == 0
    assert automaton.state == 'B'
    assert automaton.turn() == 1
    assert automaton.state == 'C'
    assert automaton.turn() == 2
    assert automaton.state == 'D'
    raises(lambda: automaton.turn(), MealyError)
    assert automaton.link() == 3
    assert automaton.state == 'E'
    assert automaton.turn() == 5
    automaton.state = 'E'
    assert automaton.link() == 6
    automaton.state = 'E'
    assert automaton.step() == 4
    assert automaton.state == 'F'
    assert automaton.turn() == 8
    assert automaton.step() == 7
    assert automaton.state == 'G'
    assert automaton.link() == 9
