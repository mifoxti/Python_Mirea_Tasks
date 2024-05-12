class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def cull(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise MealyError("cull")

    def pluck(self):
        if self.state == 'A':
            self.state = 'H'
            return 1
        elif self.state == 'C':
            self.state = 'H'
            return 4
        elif self.state == 'D':
            self.state = 'H'
            return 6
        elif self.state == 'H':
            self.state = 'E'
            return 11
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'B'
            return 10
        else:
            raise MealyError("pluck")


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
    assert automaton.pluck() == 1
    assert automaton.state == 'H'
    raises(lambda: automaton.cull(), MealyError)
    assert automaton.pluck() == 11
    assert automaton.state == 'E'
    assert automaton.pluck() == 7
    assert automaton.state == 'F'
    assert automaton.pluck() == 8
    assert automaton.state == 'G'
    assert automaton.pluck() == 10
    assert automaton.state == 'B'
    raises(lambda: automaton.pluck(), MealyError)
    assert automaton.cull() == 2
    assert automaton.state == 'C'
    assert automaton.cull() == 3
    assert automaton.state == 'D'
    assert automaton.cull() == 5
    assert automaton.pluck() == 7
    assert automaton.pluck() == 8
    assert automaton.cull() == 9
    automaton = main()
    assert automaton.pluck() == 1
    automaton = main()
    assert automaton.cull() == 0
    assert automaton.cull() == 2
    assert automaton.pluck() == 4
    automaton = main()
    assert automaton.cull() == 0
    assert automaton.cull() == 2
    assert automaton.cull() == 3
    assert automaton.pluck() == 6
