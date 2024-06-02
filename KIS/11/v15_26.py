class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def paste(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'C'
            return 7
        elif self.state == 'B':
            self.state = 'F'
            return 2
        else:
            raise MealyError("paste")

    def hike(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'E':
            self.state = 'F'
            return 5
        elif self.state == 'F':
            self.state = 'F'
            return 9
        else:
            raise MealyError("hike")

    def peep(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'E'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("peep")


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
    assert automaton.paste() == 0
    assert automaton.state == 'B'
    assert automaton.hike() == 1
    assert automaton.state == 'C'
    assert automaton.peep() == 3
    assert automaton.state == 'D'
    assert automaton.paste() == 4
    assert automaton.state == 'E'
    assert automaton.paste() == 7
    automaton.state = 'E'
    assert automaton.peep() == 6
    assert automaton.hike() == 5
    assert automaton.state == 'F'
    assert automaton.hike() == 9
    assert automaton.peep() == 8
    assert automaton.state == 'G'
    raises(lambda: automaton.hike(), MealyError)
    raises(lambda: automaton.peep(), MealyError)
    raises(lambda: automaton.paste(), MealyError)
    automaton.state = 'B'
    assert automaton.paste() == 2
