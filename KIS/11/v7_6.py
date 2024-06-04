class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def march(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'G'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise MealyError("march")

    def turn(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'D':
            self.state = 'D'
            return 5
        elif self.state == 'E':
            self.state = 'B'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'G'
            return 9
        else:
            raise MealyError("turn")


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
    assert automaton.march() == 0
    assert automaton.state == 'B'
    assert automaton.turn() == 1
    assert automaton.state == 'C'
    assert automaton.turn() == 2
    assert automaton.state == 'D'
    assert automaton.turn() == 5
    assert automaton.march() == 4
    assert automaton.state == 'E'
    assert automaton.march() == 6
    assert automaton.state == 'F'
    assert automaton.turn() == 8
    assert automaton.state == 'G'
    assert automaton.turn() == 9
    automaton.state = 'C'
    assert automaton.march() == 3
    automaton.state = 'E'
    assert automaton.turn() == 7
    automaton.state = 'None'
    raises(lambda: automaton.turn(), MealyError)
    raises(lambda: automaton.march(), MealyError)
