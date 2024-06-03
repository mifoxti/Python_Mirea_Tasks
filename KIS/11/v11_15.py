class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def share(self):
        if self.state == 'A':
            self.state = 'A'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 6
        else:
            raise MealyError("share")

    def fill(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        else:
            raise MealyError("fill")

    def drag(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError('drag')

    def scrub(self):
        if self.state == 'A':
            self.state = 'E'
            return 2
        elif self.state == 'E':
            self.state = 'C'
            return 8
        else:
            raise MealyError('scrub')


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
    assert automaton.share() == 3
    assert automaton.fill() == 0
    assert automaton.state == 'B'
    assert automaton.drag() == 4
    assert automaton.state == 'C'
    assert automaton.share() == 5
    assert automaton.state == 'D'
    assert automaton.share() == 6
    assert automaton.state == 'E'
    assert automaton.scrub() == 8
    automaton.state = 'A'
    assert automaton.drag() == 1
    automaton.state = 'A'
    assert automaton.scrub() == 2
    assert automaton.drag() == 7
    assert automaton.state == 'F'
    raises(lambda: automaton.fill(), MealyError)
    raises(lambda: automaton.scrub(), MealyError)
    raises(lambda: automaton.drag(), MealyError)
    raises(lambda: automaton.share(), MealyError)
