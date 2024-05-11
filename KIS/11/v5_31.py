class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def stay(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'C'
            return 4
        else:
            raise MealyError("stay")

    def type(self):
        if self.state == 'C':
            self.state = 'A'
            return 3
        elif self.state == 'F':
            self.state = 'A'
            return 7
        else:
            raise MealyError("type")

    def scrub(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise MealyError("scrub")


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
    raises(lambda: automaton.scrub(), MealyError)
    raises(lambda: automaton.type(), MealyError)
    assert automaton.state == 'A'
    assert automaton.stay() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.scrub(), MealyError)
    raises(lambda: automaton.type(), MealyError)
    assert automaton.stay() == 1
    assert automaton.state == 'C'
    assert automaton.stay() == 4
    assert automaton.type() == 3
    assert automaton.stay() == 0
    assert automaton.stay() == 1
    assert automaton.scrub() == 2
    assert automaton.state == 'D'
    raises(lambda: automaton.type(), MealyError)
    raises(lambda: automaton.stay(), MealyError)
    assert automaton.scrub() == 5
    assert automaton.state == 'E'
    raises(lambda: automaton.type(), MealyError)
    raises(lambda: automaton.stay(), MealyError)
    assert automaton.scrub() == 6
    assert automaton.state == 'F'
    raises(lambda: automaton.stay(), MealyError)
    assert automaton.scrub() == 8
    assert automaton.scrub() == 5
    assert automaton.scrub() == 6
    assert automaton.type() == 7
