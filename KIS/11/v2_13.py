class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def clear(self):
        if self.state == 'A':
            self.state = 'A'
            return 2
        else:
            raise MealyError('clear')

    def sort(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 4
        elif self.state == 'H':
            self.state = 'C'
            return 11
        else:
            raise MealyError("sort")

    def stash(self):
        if self.state == 'A':
            self.state = 'C'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("stash")

    def carve(self):
        if self.state == 'E':
            self.state = 'B'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 10
        elif self.state == 'A':
            self.state = 'H'
            return 1
        else:
            raise MealyError("carve")


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
    assert automaton.clear() == 2
    assert automaton.sort() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.stash(), MealyError)
    raises(lambda: automaton.clear(), MealyError)
    raises(lambda: automaton.carve(), MealyError)
    assert automaton.sort() == 4
    assert automaton.state == 'C'
    assert automaton.stash() == 5
    assert automaton.state == 'D'
    assert automaton.stash() == 6
    assert automaton.state == 'E'
    assert automaton.stash() == 7
    assert automaton.state == 'F'
    assert automaton.stash() == 9
    assert automaton.state == 'G'
    assert automaton.carve() == 10
    assert automaton.state == 'H'
    assert automaton.sort() == 11
    automaton.state = 'E'
    raises(lambda: automaton.sort(), MealyError)
    assert automaton.carve() == 8
    automaton.state = 'A'
    assert automaton.carve() == 1
    automaton.state = 'A'
    assert automaton.stash() == 3
