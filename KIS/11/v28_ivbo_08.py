class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def march(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'E'
            return 3
        elif self.state == 'E':
            self.state = 'B'
            return 6
        else:
            raise MealyError("march")

    def chip(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'E':
            self.state = 'A'
            return 5
        elif self.state == 'H':
            self.state = 'H'
            return 11
        else:
            raise MealyError("chip")

    def tread(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'E':
            self.state = 'F'
            return 4
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise MealyError("tread")

    def erase(self):
        if self.state == 'E':
            self.state = 'G'
            return 7
        elif self.state == 'H':
            self.state = 'B'
            return 10
        else:
            raise MealyError("erase")


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
    raises(lambda: automaton.tread(), MealyError)
    raises(lambda: automaton.chip(), MealyError)
    raises(lambda: automaton.erase(), MealyError)
    assert automaton.march() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.march(), MealyError)
    assert automaton.chip() == 1
    assert automaton.state == 'C'
    assert automaton.tread() == 2
    assert automaton.state == 'D'
    assert automaton.march() == 3
    assert automaton.state == 'E'
    assert automaton.chip() == 5
    assert automaton.march() == 0
    assert automaton.chip() == 1
    assert automaton.tread() == 2
    assert automaton.march() == 3
    assert automaton.march() == 6
    assert automaton.chip() == 1
    assert automaton.tread() == 2
    assert automaton.march() == 3
    assert automaton.tread() == 4
    assert automaton.state == 'F'
    assert automaton.tread() == 8
    assert automaton.state == 'G'
    assert automaton.tread() == 9
    assert automaton.state == 'H'
    assert automaton.chip() == 11
    assert automaton.erase() == 10
    automaton = main()
    assert automaton.march() == 0
    assert automaton.chip() == 1
    assert automaton.tread() == 2
    assert automaton.march() == 3
    assert automaton.erase() == 7
