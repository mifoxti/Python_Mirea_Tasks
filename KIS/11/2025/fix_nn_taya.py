class MealyError(Exception):
    pass


class MealyMachine:
    def __init__(self):
        self.current_state = 'U3'
        self._steps = 0
        self._transitions = {
            'U3': {'crush': ('U3', 'A2'),
                   'file': ('U7', 'A2'),
                   'slur': ('U6', 'A1')},
            'U7': {'throw': ('U0', 'A1')},
            'U0': {'send': ('U6', 'A1')},
            'U6': {'file': ('U2', 'A1')},
            'U2': {'file': ('U4', 'A1'),
                   'send': ('U1', 'A0')},
            'U4': {'mix': ('U5', 'A1')},
            'U5': {'slur': ('U3', 'A1'),
                   'hoard': ('U1', 'A1')},
            'U1': {'hoard': ('U4', 'A1')},
        }
        # алфавит входных символов
        self._alphabet = {
            inp
            for outs in self._transitions.values()
            for inp in outs
        }

    def run(self, inp: str) -> str:
        mapping = self._transitions.get(self.current_state, {})
        if inp not in mapping:
            if inp not in self._alphabet:
                raise MealyError('unknown')
            raise MealyError('unsupported')

        new_state, output = mapping[inp]
        self.current_state = new_state
        self._steps += 1
        return output

    def get_step(self) -> int:
        return self._steps

    def has_max_out_edges(self) -> bool:
        return len(self._transitions[self.current_state]) == 3


def main() -> MealyMachine:
    return MealyMachine()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
        assert output is None


def test():
    obj = main()
    raises(lambda: obj.run('trim'), MealyError)
    raises(lambda: obj.run('unknown'), MealyError)
    assert obj.current_state == 'U3'
    assert obj.has_max_out_edges()
    assert obj.run('crush') == 'A2'
    assert obj.run('file') == 'A2'
    assert obj.run('throw') == 'A1'
    assert obj.run('send') == 'A1'
    obj.current_state = 'U3'
    assert obj.run('slur') == 'A1'
    assert obj.run('file') == 'A1'
    assert obj.run('file') == 'A1'
    assert obj.run('mix') == 'A1'
    assert obj.run('slur') == 'A1'
    obj.current_state = 'U5'
    assert obj.run('hoard') == 'A1'
    obj.current_state = 'U2'
    assert obj.run('send') == 'A0'
    obj.get_step()
    raises(lambda: obj.run('send'), MealyError)
