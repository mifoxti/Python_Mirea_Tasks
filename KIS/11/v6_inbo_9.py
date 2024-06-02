class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def glare(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'C'
            return 4
        elif self.state == 'F':
            self.state = 'C'
            return 9
        else:
            raise MealyError('glare')

    def send(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'E':
            self.state = 'G'
            return 7
        else:
            raise MealyError("send")

    def fill(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("fill")


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
    assert automaton.glare() == 0
    assert automaton.state == 'B'
    assert automaton.send() == 2
    assert automaton.state == 'C'
    automaton.state = 'A'
    assert automaton.send() == 1
    assert automaton.glare() == 4
    assert automaton.fill() == 3
    assert automaton.state == 'D'
    assert automaton.fill() == 5
    assert automaton.state == 'E'
    assert automaton.fill() == 6
    assert automaton.state == 'F'
    assert automaton.glare() == 9
    automaton.state = 'E'
    assert automaton.send() == 7
    assert automaton.state == 'G'
    automaton.state = 'F'
    assert automaton.fill() == 8
    raises(lambda: automaton.send(), MealyError)
    raises(lambda: automaton.fill(), MealyError)
    raises(lambda: automaton.glare(), MealyError)
