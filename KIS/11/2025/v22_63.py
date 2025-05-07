class MachineError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'G0'

        self.conditional_transitions = {
            'G0': {
                'leer': [({}, 'G6', 'V0')]
            },
            'G6': {
                'play': [({'v': 0}, 'G6', 'V1'),
                         ({'v': 1}, 'G1', 'V0')],
                'stash': [({}, 'G5', 'V1')],
            },
            'G5': {
                'stash': [({}, 'G1', 'V0')],
            },
            'G1': {
                'play': [({'p': 1}, 'G1', 'V1'),
                         ({'p': 0}, 'G3', 'V0')],
            },
            'G3': {
                'stash': [({'f': 0}, 'G5', 'V1'),
                          ({'f': 1}, 'G2', 'V1')],
            },
            'G2': {
                'peek': [({}, 'G4', 'V0')],
            },
        }
        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.executed_methods = set()

    def has_max_out_edges(self):
        out_counts = {}
        for state, transitions in self.conditional_transitions.items():
            count = 0
            for action, variants in transitions.items():
                count += len(variants)
            out_counts[state] = count

        max_out = max(out_counts.values(), default=0)
        return out_counts.get(self.state, 0) == max_out

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def seen_edge(self, from_state, to_state):
        return self.transition_counts.get((from_state, to_state), 0)

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            raise MachineError('unsupported')

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts.get((self.state,
                                                    to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.executed_methods.add(name)
                return output

        raise MachineError('unsupported')

    def get_step(self):
        return self.step_count

    def __getattr__(self, name):
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        name = name.lstrip('run_')
        if not self._trigger_exists(name):
            raise MachineError('unknown')
        return lambda: (self._try_apply_trigger(name) or None)


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
    obj.has_max_out_edges()  # False
    assert obj.state == 'G0'
    obj.f(1)
    obj.vars.clear()
    assert obj.run_leer() == 'V0'
    obj.seen_edge('G0', 'G6')
    obj.get_step()
    raises(lambda: obj.run_play(), MachineError)
    obj.v(0)
    assert obj.run_play() == 'V1'
    obj.v(1)
    assert obj.run_play() == 'V0'
    obj.state = 'G6'
    assert obj.run_stash() == 'V1'
    assert obj.run_stash() == 'V0'
    obj.p(1)
    assert obj.run_play() == 'V1'
    obj.p(0)
    assert obj.run_play() == 'V0'
    obj.f(0)
    assert obj.run_stash() == 'V1'
    obj.state = 'G3'
    obj.f(1)
    assert obj.run_stash() == 'V1'
    assert obj.run_peek() == 'V0'
    raises(lambda: obj.run_ne_run(), MachineError)
    raises(lambda: obj.run_peek(), MachineError)
