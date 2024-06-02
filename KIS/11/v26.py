class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def loop(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 7
        elif self.state == 'G':
            self.state = 'H'
            return 10
        elif self.state == 'H':
            self.state = 'D'
            return 11
        else:
            raise MealyError("loop")

    def stare(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'B':
            self.state = 'G'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 8
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("stare")

    def play(self):
        if self.state == 'B':
            self.state = 'E'
            return 4
        elif self.state == 'C':
            self.state = 'H'
            return 6
        else:
            raise MealyError("play")


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
    assert automaton.loop() == 0
    assert automaton.state == 'B'
    assert automaton.loop() == 2
    assert automaton.state == 'C'
    assert automaton.loop() == 5
    assert automaton.state == 'D'
    assert automaton.loop() == 7
    assert automaton.state == 'E'
    assert automaton.stare() == 8
    assert automaton.state == 'F'
    assert automaton.stare() == 9
    assert automaton.state == 'G'
    assert automaton.loop() == 10
    assert automaton.state == 'H'
    assert automaton.loop() == 11
    automaton.state = 'A'
    assert automaton.stare() == 1
    assert automaton.play() == 6
    automaton.state = 'B'
    assert automaton.play() == 4
    automaton.state = 'B'
    assert automaton.stare() == 3
    automaton.state = 'None'
    raises(lambda: automaton.loop(), MealyError)
    raises(lambda: automaton.stare(), MealyError)
    raises(lambda: automaton.play(), MealyError)
