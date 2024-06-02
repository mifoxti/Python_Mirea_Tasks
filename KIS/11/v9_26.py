class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def punch(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("punch")

    def visit(self):
        if self.state == 'C':
            self.state = 'A'
            return 4
        elif self.state == 'F':
            self.state = 'C'
            return 9
        else:
            raise MealyError("visit")

    def jump(self):
        if self.state == 'C':
            self.state = 'E'
            return 5
        elif self.state == 'A':
            self.state = 'E'
            return 1
        else:
            raise MealyError("jump")


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
    assert automaton.punch() == 0
    assert automaton.state == 'B'
    assert automaton.punch() == 2
    assert automaton.state == 'C'
    assert automaton.punch() == 3
    assert automaton.state == 'D'
    assert automaton.punch() == 6
    assert automaton.state == 'E'
    assert automaton.punch() == 7
    assert automaton.state == 'F'
    assert automaton.punch() == 8
    assert automaton.state == 'G'
    automaton.state = 'F'
    assert automaton.visit() == 9
    assert automaton.visit() == 4
    assert automaton.jump() == 1
    automaton.state = 'C'
    assert automaton.jump() == 5
    automaton.state = 'G'
    raises(lambda: automaton.jump(), MealyError)
    raises(lambda: automaton.punch(), MealyError)
    raises(lambda: automaton.visit(), MealyError)
