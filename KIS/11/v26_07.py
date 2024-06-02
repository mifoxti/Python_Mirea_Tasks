class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def cull(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'A'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'G'
            return 7
        elif self.state == 'G':
            self.state = 'D'
            return 9
        else:
            raise MealyError('cull')

    def clone(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise MealyError("clone")


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
    assert automaton.cull() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.cull(), MealyError)
    assert automaton.clone() == 2
    assert automaton.state == 'C'
    assert automaton.cull() == 4
    assert automaton.clone() == 1
    automaton.state = 'C'
    assert automaton.clone() == 3
    assert automaton.state == 'D'
    raises(lambda: automaton.clone(), MealyError)
    assert automaton.cull() == 5
    assert automaton.state == 'E'
    assert automaton.clone() == 6
    assert automaton.state == 'F'
    assert automaton.clone() == 8
    automaton.state = 'F'
    assert automaton.cull() == 7
    assert automaton.state == 'G'
    assert automaton.cull() == 9
