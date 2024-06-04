class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def place(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'F'
            return 5
        elif self.state == 'F':
            self.state = 'B'
            return 8
        else:
            self.state = 'F'
            return 6

    def loop(self):
        if self.state == 'B':
            self.state = 'B'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'F':
            self.state = 'A'
            return 7
        else:
            raise MealyError("loop")


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
    assert automaton.place() == 0
    assert automaton.loop() == 2
    assert automaton.state == 'B'
    assert automaton.place() == 1
    assert automaton.state == 'C'
    assert automaton.place() == 3
    assert automaton.state == 'D'
    assert automaton.loop() == 4
    assert automaton.state == 'E'
    assert automaton.place() == 6
    assert automaton.state == 'F'
    automaton.state = 'D'
    assert automaton.place() == 5
    assert automaton.place() == 8
    automaton.state = 'F'
    assert automaton.loop() == 7
    raises(lambda: automaton.loop(), MealyError)
