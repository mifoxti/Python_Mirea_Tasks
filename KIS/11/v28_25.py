class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def cull(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'E':
            self.state = 'F'
            return 4
        elif self.state == 'F':
            self.state = 'C'
            return 7
        elif self.state == 'G':
            self.state = 'B'
            return 9
        else:
            raise MealyError("cull")

    def fade(self):
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
            self.state = 'G'
            return 5
        elif self.state == 'G':
            self.state = 'D'
            return 8
        elif self.state == 'F':
            self.state = 'G'
            return 6
        else:
            raise MealyError("fade")


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
    raises(lambda: automaton.fade(), MealyError)
    assert automaton.cull() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.cull(), MealyError)
    assert automaton.fade() == 1
    assert automaton.state == 'C'
    assert automaton.fade() == 2
    assert automaton.state == 'D'
    assert automaton.fade() == 3
    assert automaton.state == 'E'
    assert automaton.fade() == 5
    assert automaton.state == 'G'
    automaton.state = 'E'
    assert automaton.cull() == 4
    assert automaton.state == 'F'
    assert automaton.cull() == 7
    automaton.state = 'F'
    assert automaton.fade() == 6
    assert automaton.fade() == 8
    automaton.state = 'G'
    assert automaton.cull() == 9
