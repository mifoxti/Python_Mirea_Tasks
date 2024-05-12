class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def rock(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'B'
            return 5
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("rock")

    def move(self):
        if self.state == 'A':
            self.state = 'F'
            return 2
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 6
        else:
            raise MealyError("move")

    def add(self):
        if self.state == 'A':
            self.state = 'G'
            return 1
        elif self.state == 'D':
            self.state = 'E'
            return 7
        elif self.state == 'E':
            self.state = 'F'
            return 8
        else:
            raise MealyError("add")


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
    assert automaton.rock() == 0
    assert automaton.state == 'B'
    assert automaton.rock() == 5
    assert automaton.move() == 3
    assert automaton.state == 'C'
    raises(lambda: automaton.add(), MealyError)
    raises(lambda: automaton.rock(), MealyError)
    assert automaton.move() == 6
    assert automaton.state == 'D'
    raises(lambda: automaton.move(), MealyError)
    assert automaton.add() == 7
    assert automaton.state == 'E'
    assert automaton.add() == 8
    assert automaton.state == 'F'
    assert automaton.rock() == 9
    assert automaton.state == 'G'
    automaton = main()
    assert automaton.move() == 2
    automaton = main()
    assert automaton.add() == 1
