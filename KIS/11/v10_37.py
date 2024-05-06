class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def run(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'F'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'E':
            self.state = 'C'
            return 8
        else:
            raise MealyError("run")

    def fade(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'D':
            self.state = 'F'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError("fade")

    def pluck(self):
        if self.state == 'B':
            self.state = 'E'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 5
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
    raises(lambda: automaton.pluck(), MealyError)
    raises(lambda: automaton.fade(), MealyError)
    assert automaton.state == 'A'
    assert automaton.run() == 0
    assert automaton.state == 'B'
    assert automaton.fade() == 1
    assert automaton.state == 'C'
    raises(lambda: automaton.pluck(), MealyError)
    raises(lambda: automaton.fade(), MealyError)
    assert automaton.run() == 4
    assert automaton.state == 'D'
    raises(lambda: automaton.run(), MealyError)
    assert automaton.pluck() == 5
    assert automaton.state == 'E'
    raises(lambda: automaton.pluck(), MealyError)
    assert automaton.run() == 8
    assert automaton.run() == 4
    assert automaton.fade() == 6
    assert automaton.state == 'F'
    raises(lambda: automaton.pluck(), MealyError)
    raises(lambda: automaton.fade(), MealyError)
    raises(lambda: automaton.run(), MealyError)
    automaton = main()
    assert automaton.run() == 0
    assert automaton.pluck() == 2
    assert automaton.fade() == 7
    automaton = main()
    assert automaton.run() == 0
    assert automaton.run() == 3
