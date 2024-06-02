class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def base(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'E'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise MealyError("base")

    def paste(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'C'
            return 4
        elif self.state == 'D':
            self.state = 'D'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise MealyError("paste")


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
    assert automaton.base() == 0
    assert automaton.state == 'B'
    assert automaton.base() == 2
    assert automaton.state == 'E'
    assert automaton.paste() == 7
    assert automaton.state == 'F'
    assert automaton.paste() == 8
    assert automaton.state == 'D'
    assert automaton.paste() == 6
    assert automaton.base() == 5
    automaton.state = 'B'
    assert automaton.paste() == 1
    assert automaton.state == 'C'
    assert automaton.paste() == 4
    assert automaton.base() == 3
    automaton.state = 'None'
    raises(lambda: automaton.paste(), MealyError)
    raises(lambda: automaton.base(), MealyError)
