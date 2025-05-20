class MachineException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'c5'

        self.conditional_transitions = {
            'c5': {
                'pull': [({'v': 0}, 'c3', 'f2'),
                         ({'v': 1}, 'c0', 'f1')],
            },
            'c3': {
                'cast': [({'z': 0}, 'c0', 'f1'),
                         ({'z': 1}, 'c2', 'f1')],
            },
            'c0': {
                'cast': [({}, 'c6', 'f1'), ],
                'pull': [({}, 'c1', 'f2'), ]
            },
            'c6': {
                'clean': [({}, 'c4', 'f2'), ],
            },
            'c4': {
                'skid': [({}, 'c1', 'f2'), ],
            },
            'c1': {
                'pull': [({}, 'c2', 'f1')],
            },
            'c2': {
                'look': [({}, 'c5', 'f1'), ],
            }
        }
        self.transition_counts = {}
        self.vars = {}
        self.executed_methods = set()
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['c5']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def move(self, command):
        if not self._trigger_exists(command):
            raise MachineException('unknown')

        current_transitions = self.conditional_transitions.get(self.state, {})
        if command not in current_transitions:
            raise MachineException('unsupported')

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
                return None
        raise MachineException('unsupported')

    def seen_method(self, method):
        return True if method in self.executed_methods else False

    def has_max_out_edges(self):
        return True if self.state in ['c5', 'c3', 'c0'] else False

    def get_output(self):
        return self.last_output

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
    raises(lambda: obj.move('pull'), MachineException)
    raises(lambda: obj.obama(), MachineException)
    assert obj.z(1) is None
    assert obj.v(1) is None
    assert obj.move('pull') is None
    raises(lambda: obj.move('slog'), MachineException)

    assert obj.v(0) is None
    assert obj.get_output() == 'f1'
    assert obj.move('cast') is None
    assert obj.get_output() == 'f1'
    raises(lambda: obj.move('blame'), MachineException)

    assert obj.has_max_out_edges() is False
    assert obj.seen_method('cast') is True
    assert obj.has_max_out_edges() is False
    assert obj.move('clean') is None
    assert obj.get_output() == 'f2'
    assert obj.has_max_out_edges() is False
    assert obj.move('skid') is None
    assert obj.get_output() == 'f2'
    assert obj.has_max_out_edges() is False
    raises(lambda: obj.move('blame'), MachineException)

    assert obj.move('pull') is None
    assert obj.get_output() == 'f1'
    raises(lambda: obj.move('blame'), MachineException)

    assert obj.move('look') is None
    assert obj.get_output() == 'f1'
    assert obj.has_max_out_edges() is True
    assert obj.move('pull') is None
    raises(lambda: obj.move('check'), MachineException)

    assert obj.v(0) is None
    assert obj.get_output() == 'f2'
    raises(lambda: obj.move('skid'), MachineException)
    assert obj.move('cast') is None
    raises(lambda: obj.move('slog'), MachineException)
    assert obj.get_output() == 'f1'
    assert obj.move('look') is None
    assert obj.get_output() == 'f1'
    assert obj.move('pull') is None
    assert obj.get_output() == 'f2'
    raises(lambda: obj.move('clean'), MachineException)
