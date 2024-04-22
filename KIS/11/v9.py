class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def begin(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'G':
            self.state = 'G'
            return 11
        else:
            raise MealyError("begin")

    def blame(self):
        if self.state == 'A':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'D'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise MealyError("blame")

    def tail(self):
        if self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'A':
            self.state = 'G'
            return 1
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 7
        elif self.state == 'G':
            self.state = 'E'
            return 10
        else:
            raise MealyError("tail")


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
    assert automaton.begin() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.blame(), MealyError)
    raises(lambda: automaton.begin(), MealyError)
    assert automaton.tail() == 3
    assert automaton.state == 'C'
    raises(lambda: automaton.begin(), MealyError)
    raises(lambda: automaton.tail(), MealyError)
    assert automaton.blame() == 4
    assert automaton.state == 'D'
    raises(lambda: automaton.begin(), MealyError)
    raises(lambda: automaton.tail(), MealyError)
    assert automaton.blame() == 5
    assert automaton.state == 'E'
    raises(lambda: automaton.blame(), MealyError)
    raises(lambda: automaton.begin(), MealyError)
    assert automaton.tail() == 6
    assert automaton.state == 'F'
    raises(lambda: automaton.begin(), MealyError)
    assert automaton.blame() == 8
    assert automaton.blame() == 5
    assert automaton.tail() == 6
    assert automaton.tail() == 7
    assert automaton.state == 'G'
    assert automaton.tail() == 10

    automaton = main()
    assert automaton.tail() == 1
    assert automaton.begin() == 11
    assert automaton.blame() == 9
    assert automaton.state == 'H'
    raises(lambda: automaton.begin(), MealyError)
    raises(lambda: automaton.tail(), MealyError)
    raises(lambda: automaton.blame(), MealyError)

    automaton = main()
    assert automaton.blame() == 2
