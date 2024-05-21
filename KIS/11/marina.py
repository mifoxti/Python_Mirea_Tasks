class MealyError(Exception):
    pass


class MealyAutomat:
    def __init__(self):
        self.state = 'A'

    def leer(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'F'
            return 4
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("leer")

    def smash(self):
        if self.state == 'A':
            self.state = 'G'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'G':
            self.state = 'E'
            return 9
        else:
            raise MealyError("smash")

    def grow(self):
        if self.state == 'A':
            self.state = 'F'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 5
        else:
            raise MealyError("grow")


def main():
    return MealyAutomat()


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
    assert automaton.leer() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.grow(), MealyError)
    assert automaton.smash() == 3
    assert automaton.state == 'C'
    raises(lambda: automaton.leer(), MealyError)
    raises(lambda: automaton.smash(), MealyError)
    assert automaton.grow() == 5
    assert automaton.state == 'D'
    assert automaton.smash() == 6
    assert automaton.state == 'E'
    assert automaton.smash() == 7
    assert automaton.state == 'F'
    assert automaton.leer() == 8
    assert automaton.state == 'G'
    assert automaton.smash() == 9
    automaton.state = 'B'
    assert automaton.leer() == 4
    automaton.state = 'A'
    assert automaton.grow() == 2
    automaton.state = 'A'
    assert automaton.smash() == 1
