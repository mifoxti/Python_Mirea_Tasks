class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def look(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'B'
            return 4
        elif self.state == 'E':
            self.state = 'E'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("look")

    def run(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'D':
            self.state = 'E'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise MealyError("run")

    def scrub(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'D':
            self.state = 'D'
            return 5
        elif self.state == 'F':
            self.state = 'H'
            return 9
        elif self.state == 'H':
            self.state = 'H'
            return 11
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
    assert automaton.state == 'A'
    raises(lambda: automaton.run(), MealyError)
    raises(lambda: automaton.scrub(), MealyError)
    assert automaton.look() == 0
    raises(lambda: automaton.look(), MealyError)
    assert automaton.state == 'B'
    assert automaton.run() == 1
    assert automaton.state == 'C'
    assert automaton.scrub() == 2
    assert automaton.state == 'D'
    assert automaton.scrub() == 5
    assert automaton.look() == 4
    assert automaton.run() == 1
    assert automaton.scrub() == 2
    assert automaton.run() == 3
    assert automaton.state == 'E'
    assert automaton.look() == 7
    assert automaton.run() == 6
    assert automaton.state == 'F'
    assert automaton.look() == 8
    assert automaton.state == 'G'
    assert automaton.run() == 10
    assert automaton.state == 'H'
    assert automaton.scrub() == 11
    automaton = main()
    assert automaton.look() == 0
    assert automaton.run() == 1
    assert automaton.scrub() == 2
    assert automaton.run() == 3
    assert automaton.run() == 6
    assert automaton.scrub() == 9
