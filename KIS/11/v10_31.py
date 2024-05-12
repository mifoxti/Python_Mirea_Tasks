class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def amass(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'E'
            return 3
        elif self.state == 'C':
            self.state = 'E'
            return 6
        else:
            raise MealyError("amass")

    def pull(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'F'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 7
        elif self.state == 'E':
            self.state = 'F'
            return 8
        else:
            raise MealyError("pull")

    def make(self):
        if self.state == 'B':
            self.state = 'D'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        else:
            raise MealyError("make")


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
    raises(lambda: automaton.make(), MealyError)
    raises(lambda: automaton.pull(), MealyError)
    assert automaton.amass() == 0
    assert automaton.state == 'B'
    assert automaton.pull() == 1
    assert automaton.state == 'C'
    assert automaton.make() == 4
    assert automaton.state == 'D'
    assert automaton.pull() == 7
    raises(lambda: automaton.amass(), MealyError)
    assert automaton.state == 'E'
    assert automaton.pull() == 8
    assert automaton.state == 'F'
    automaton = main()
    assert automaton.amass() == 0
    assert automaton.pull() == 1
    assert automaton.amass() == 6
    automaton = main()
    assert automaton.amass() == 0
    assert automaton.pull() == 1
    assert automaton.pull() == 5
    automaton = main()
    assert automaton.amass() == 0
    assert automaton.make() == 2
    automaton = main()
    assert automaton.amass() == 0
    assert automaton.amass() == 3
