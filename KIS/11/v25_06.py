class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def view(self):
        if self.state == 'A':
            self.state = 'A'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'G':
            self.state = 'G'
            return 9
        else:
            raise MealyError("view")

    def link(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 6
        else:
            raise MealyError("link")

    def push(self):
        if self.state == 'A':
            self.state = 'F'
            return 1
        elif self.state == 'B':
            self.state = 'F'
            return 4
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError("push")


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
    assert automaton.view() == 2
    assert automaton.link() == 0
    assert automaton.state == 'B'
    raises(lambda: automaton.view(), MealyError)
    assert automaton.link() == 3
    assert automaton.state == 'C'
    raises(lambda: automaton.push(), MealyError)
    raises(lambda: automaton.link(), MealyError)
    assert automaton.view() == 5
    assert automaton.state == 'D'
    raises(lambda: automaton.push(), MealyError)
    raises(lambda: automaton.view(), MealyError)
    assert automaton.link() == 6
    assert automaton.state == 'E'
    raises(lambda: automaton.push(), MealyError)
    raises(lambda: automaton.link(), MealyError)
    assert automaton.view() == 7
    assert automaton.state == 'F'
    raises(lambda: automaton.link(), MealyError)
    raises(lambda: automaton.view(), MealyError)
    assert automaton.push() == 8
    assert automaton.state == 'G'
    raises(lambda: automaton.push(), MealyError)
    raises(lambda: automaton.link(), MealyError)
    assert automaton.view() == 9
    automaton = main()
    assert automaton.link() == 0
    assert automaton.push() == 4
    automaton = main()
    assert automaton.push() == 1
