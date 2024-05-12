class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def rush(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'G'
            return 8
        elif self.state == 'F':
            self.state = 'G'
            return 9
        else:
            raise MealyError("rush")

    def cast(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'E':
            self.state = 'C'
            return 7
        elif self.state == 'F':
            self.state = 'C'
            return 10
        else:
            raise MealyError("cast")

    def unite(self):
        if self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'G':
            self.state = 'H'
            return 11
        else:
            raise MealyError("unite")


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
    raises(lambda: automaton.unite(), MealyError)
    assert automaton.state == 'A'
    assert automaton.rush() == 0
    assert automaton.state == 'B'
    assert automaton.rush() == 3
    assert automaton.state == 'D'
    raises(lambda: automaton.rush(), MealyError)
    raises(lambda: automaton.cast(), MealyError)
    assert automaton.unite() == 5
    assert automaton.state == 'E'
    assert automaton.unite() == 6
    assert automaton.state == 'F'
    assert automaton.cast() == 10
    assert automaton.cast() == 4
    assert automaton.unite() == 5
    assert automaton.cast() == 7
    assert automaton.state == 'C'
    assert automaton.cast() == 4
    assert automaton.unite() == 5
    assert automaton.rush() == 8
    assert automaton.state == 'G'
    assert automaton.unite() == 11
    assert automaton.state == 'H'
    automaton = main()
    assert automaton.rush() == 0
    assert automaton.cast() == 2
    assert automaton.cast() == 4
    assert automaton.unite() == 5
    assert automaton.unite() == 6
    assert automaton.rush() == 9
    automaton = main()
    assert automaton.cast() == 1
