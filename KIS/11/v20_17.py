class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def order(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'F'
            return 2
        elif self.state == 'F':
            self.state = 'C'
            return 7
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 4
        else:
            self.state = 'F'
            return 5

    def amass(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'E':
            self.state = 'B'
            return 6
        elif self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise MealyError("amass")


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
    raises(lambda: automaton.amass(), MealyError)
    assert automaton.order() == 0
    assert automaton.state == 'B'
    assert automaton.order() == 2
    assert automaton.state == 'F'
    assert automaton.order() == 7
    assert automaton.state == 'C'
    assert automaton.order() == 3
    assert automaton.state == 'D'
    assert automaton.order() == 4
    assert automaton.state == 'E'
    assert automaton.order() == 5
    assert automaton.state == 'F'
    assert automaton.order() == 7
    automaton.state = 'F'
    assert automaton.amass() == 8
    automaton.state = 'E'
    assert automaton.amass() == 6
    assert automaton.amass() == 1
