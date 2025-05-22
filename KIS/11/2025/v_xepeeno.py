class MealyAutomat:
    def __init__(self):
        self.state = 'w1'

        self.conditional_transitions = {
            'w1': {
                'crush': [({}, 'w2', 'V2')],
            },
            'w2': {
                'load': [({}, 'w5', 'V0'), ],
            },
            'w5': {
                'check': [({'m': 1}, 'w0', 'V2'),
                          ({'m': 0}, 'w3', 'V2'), ],
            },
            'w0': {
                'merge': [({}, 'w1', 'V1')],
                'lower': [({}, 'w3', 'V2')],
            },
            'w3': {
                'load': [({}, 'w2', 'V1')],
                'check': [({'f': 1}, 'w4', 'V2'),
                          ({'f': 0}, 'w0', 'V1'), ],
            },
            'w4': {
                'merge': [({}, 'w6', 'V2')],
            },
        }
        self.transition_counts = {}
        self.vars = {}
        self.executed_methods = set()
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['w1']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = (
            self.conditional_transitions.get(self.state, {})
        )
        if name not in current_transitions:
            return 'unsupported'

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts
                        .get((self.state, to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.executed_states.append(self.state)
                self.last_state = output
                self.executed_methods.add(name)
                return output
        return 'unsupported'

    def get_step(self):
        return self.step_count

    def seen_method(self, method):
        return True if method in self.executed_methods else False

    def part_of_loop(self):
        return True if self.state not in ['w4', 'w6'] else False

    def __getattr__(self, name):
        name = name.replace('store_', '').replace('run_', '')
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        if not self._trigger_exists(name):
            return lambda: "unknown"
        return lambda: (self._try_apply_trigger(name) or None)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.seen_method('merge') is False
    assert obj.run_merge() == 'unsupported'
    assert obj.store_f(1) is None
    assert obj.seen_method('lower') is False
    assert obj.run_order() == 'unknown'
    assert obj.run_crush() == 'V2'
    assert obj.run_load() == 'V0'
    assert obj.seen_method('load') is True
    assert obj.run_check() == 'unsupported'
    assert obj.store_m(0) is None
    assert obj.run_check() == 'V2'
    assert obj.part_of_loop() is True
    assert obj.run_check() == 'V2'
    assert obj.run_load() == 'unsupported'
    assert obj.get_step() == 4
    assert obj.part_of_loop() is False
    assert obj.run_merge() == 'V2'
    assert obj.run_drag() == 'unknown'
    assert obj.get_step() == 5
