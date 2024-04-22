class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def etch(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'G'
            return 4
        elif self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 8
        else:
            raise MealyError("etch")

    def click(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'B':
            self.state = 'F'
            return 3
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("click")

    def boost(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'D':
            self.state = 'A'
            return 7
        else:
            raise MealyError("boost")


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
    raises(lambda: automaton.boost(), MealyError)
    assert automaton.state == 'A'
    assert automaton.etch() == 0
    assert automaton.state == 'B'
    assert automaton.etch() == 4
    assert automaton.state == 'G'
    raises(lambda: automaton.boost(), MealyError)
    raises(lambda: automaton.etch(), MealyError)
    raises(lambda: automaton.click(), MealyError)

    automaton = main()
    assert automaton.etch() == 0
    assert automaton.click() == 3
    assert automaton.state == 'F'
    assert automaton.click() == 9

    automaton = main()
    assert automaton.etch() == 0
    assert automaton.boost() == 2
    assert automaton.state == 'C'
    raises(lambda: automaton.boost(), MealyError)
    raises(lambda: automaton.click(), MealyError)
    assert automaton.etch() == 5
    raises(lambda: automaton.etch(), MealyError)
    assert automaton.state == 'D'
    assert automaton.boost() == 7
    assert automaton.click() == 1
    assert automaton.etch() == 5
    assert automaton.click() == 6
    assert automaton.state == 'E'
    raises(lambda: automaton.boost(), MealyError)
    raises(lambda: automaton.click(), MealyError)
    assert automaton.etch() == 8
