class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def peek(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'F'
            return 5
        else:
            raise MealyError('peek')

    def amble(self):
        if self.state == 'A':
            self.state = 'F'
            return 1
        elif self.state == 'F':
            self.state = 'B'
            return 8
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise MealyError("amble")

    def move(self):
        if self.state == 'E':
            self.state = 'E'
            return 7
        else:
            raise MealyError("move")


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
    assert automaton.peek() == 0
    assert automaton.state == 'B'
    assert automaton.amble() == 2
    assert automaton.state == 'C'
    assert automaton.peek() == 3
    assert automaton.state == 'D'
    assert automaton.amble() == 4
    assert automaton.state == 'E'
    assert automaton.move() == 7
    assert automaton.amble() == 6
    assert automaton.state == 'F'
    assert automaton.amble() == 8
    automaton.state = 'D'
    assert automaton.peek() == 5
    automaton.state = 'A'
    assert automaton.amble() == 1
    automaton.state = 'None'
    raises(lambda: automaton.move(), MealyError)
    raises(lambda: automaton.peek(), MealyError)
    raises(lambda: automaton.amble(), MealyError)
