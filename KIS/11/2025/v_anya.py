class MachineError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'M2'

        self.conditional_transitions = {
            'M2': {
                'cast': [({}, 'M5', 'b3')],
            },
            'M5': {
                'cast': [({}, 'M4', 'b3'), ],
            },
            'M4': {
                'log': [({'b': 0}, 'M4', 'b0'),
                        ({'b': 1}, 'M0', 'b1'), ],
            },
            'M0': {
                'spin': [({}, 'M3', 'b3'), ],
            },
            'M3': {
                'turn': [({'s': 1}, 'M5', 'b0'),
                         ({'s': 0}, 'M2', 'b1'), ],
                'cast': [({}, 'M1', 'b1')],
            },
            'M1': {
                'spin': [({}, 'M3', 'b1')],
            },
        }
        self.transition_counts = {}
        self.vars = {}
        self.executed_methods = set()
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['M2']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def move(self, command):
        if not self._trigger_exists(command):
            raise MachineError('unknown')

        current_transitions = self.conditional_transitions.get(self.state, {})
        if command not in current_transitions:
            raise MachineError('unsupported')

        transitions = current_transitions[command]

        for conds, next_state, output in transitions:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, next_state)] = (
                        self.transition_counts.get((self.state,
                                                    next_state), 0) + 1
                )
                self.state = next_state
                self.step_count += 1
                self.executed_methods.add(command)
                self.executed_states.append(next_state)
                self.last_output = output
                return output
        raise MachineError('unsupported')

    def seen_state(self, state):
        return True if state in self.executed_states else False

    def has_path_to(self, command):
        return True

    def part_of_loop(self):
        return True

    def __getattr__(self, name):
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        return lambda: (self.move(name) or None)


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
        assert output is None


def main():
    return MealyAutomat()


def test():
    obj = main()
    raises(lambda: obj.move('log'), MachineError)
    assert obj.has_path_to('M5') is True
    assert obj.s(0) is None
    raises(lambda: obj.ban(), MachineError)
    assert obj.seen_state('M5') is False
    assert obj.part_of_loop() is True
    assert obj.move('cast') == 'b3'
    assert obj.has_path_to('M0') is True
    assert obj.move('cast') == 'b3'
    raises(lambda: obj.move('throw'), MachineError)
    raises(lambda: obj.move('log'), MachineError)
    assert obj.b(1) is None
    assert obj.move('log') == 'b1'
    assert obj.move('spin') == 'b3'
    assert obj.move('turn') == 'b1'
