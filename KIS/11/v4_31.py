class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def flip(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'F'
            return 4
        elif self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError("flip")

    def sort(self):
        if self.state == 'A':
            self.state = 'G'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'D'
            return 9
        else:
            raise MealyError("sort")

    def march(self):
        if self.state == 'A':
            self.state = 'E'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 6
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
    assert automaton.state == 'A'
    assert automaton.sort() == 1
    assert automaton.state == 'G'
    raises(lambda: automaton.flip(), MealyError)
    raises(lambda: automaton.march(), MealyError)
    assert automaton.sort() == 9
    assert automaton.state == 'D'
    raises(lambda: automaton.sort(), MealyError)
    assert automaton.march() == 6
    assert automaton.state == 'E'
    assert automaton.flip() == 7
    assert automaton.state == 'F'
    assert automaton.sort() == 8
    automaton = main()
    assert automaton.flip() == 0
    assert automaton.state == 'B'
    assert automaton.sort() == 3
    assert automaton.state == 'C'
    assert automaton.flip() == 5
    automaton = main()
    assert automaton.flip() == 0
    assert automaton.flip() == 4
    automaton = main()
    assert automaton.march() == 2
