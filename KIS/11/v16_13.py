class MealyError(Exception):
    pass


class MealyAutomaton:
    def __init__(self):
        self.state = 'A'

    def chat(self):
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
            return 4
        elif self.state == 'E':
            self.state = 'E'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 7
        else:
            raise MealyError("chat")

    def log(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        elif self.state == 'F':
            self.state = 'D'
            return 8
        elif self.state == 'G':
            self.state = 'A'
            return 9
        else:
            raise MealyError("log")

    def stop(self):
        if self.state == 'E':
            self.state = 'F'
            return 5
        else:
            raise MealyError("stop")


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
    assert automaton.chat() == 0
    assert automaton.state == 'B'
    assert automaton.chat() == 2
    assert automaton.state == 'C'
    assert automaton.chat() == 3
    assert automaton.state == 'D'
    assert automaton.chat() == 4
    assert automaton.state == 'E'
    assert automaton.chat() == 6
    assert automaton.stop() == 5
    assert automaton.state == 'F'
    assert automaton.log() == 8
    automaton.state = 'F'
    assert automaton.chat() == 7
    assert automaton.state == 'G'
    assert automaton.log() == 9
    assert automaton.log() == 1
    automaton.state = 'G'
    raises(lambda: automaton.chat(), MealyError)
    raises(lambda: automaton.stop(), MealyError)
    automaton.state = 'D'
    raises(lambda: automaton.log(), MealyError)
