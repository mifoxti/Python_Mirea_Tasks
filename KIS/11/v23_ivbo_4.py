class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def clean(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 7
        else:
            raise MealyError("clean")

    def march(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'C'
            return 3
        elif self.state == 'D':
            self.state = 'D'
            return 5
        elif self.state == 'F':
            self.state = 'A'
            return 8
        elif self.state == 'G':
            self.state = 'A'
            return 9
        else:
            raise MealyError("march")


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
    raises(lambda: automaton.clean(), MealyError)
    assert automaton.state == 'A'
    assert automaton.march() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.march(), MealyError)
    assert automaton.clean() == 1
    assert automaton.state == 'C'
    assert automaton.march() == 3
    assert automaton.clean() == 2
    assert automaton.state == 'D'
    assert automaton.march() == 5
    assert automaton.clean() == 4
    assert automaton.state == 'E'
    assert automaton.clean() == 6
    assert automaton.state == 'F'
    assert automaton.march() == 8
    automaton.state = 'F'
    assert automaton.clean() == 7
    assert automaton.state == 'G'
    assert automaton.march() == 9
