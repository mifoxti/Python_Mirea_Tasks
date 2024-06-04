class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def wreck(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'E'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'A'
            return 8
        else:
            raise MealyError("wreck")

    def move(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'C'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError("move")

    def chalk(self):
        if self.state == 'D':
            self.state = 'D'
            return 6
        else:
            raise MealyError("chalk")


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
    assert automaton.wreck() == 0
    assert automaton.state == 'B'
    assert automaton.move() == 1
    assert automaton.state == 'C'
    assert automaton.move() == 4
    assert automaton.wreck() == 3
    assert automaton.state == 'D'
    assert automaton.chalk() == 6
    assert automaton.wreck() == 5
    assert automaton.state == 'E'
    automaton.state = 'B'
    assert automaton.wreck() == 2
    assert automaton.move() == 7
    assert automaton.state == 'F'
    assert automaton.wreck() == 8
    automaton.state = 'None'
    raises(lambda: automaton.chalk(), MealyError)
    raises(lambda: automaton.wreck(), MealyError)
    raises(lambda: automaton.move(), MealyError)
