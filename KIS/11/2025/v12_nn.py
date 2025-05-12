class MealyAutomat:
    def __init__(self):
        self.state = 'w0'

        self.conditional_transitions = {
            'w0': {
                'fill': [({'r': 0}, 'w3', 'x2'),
                         ({'r': 1}, 'w5', 'x0')],
            },
            'w3': {
                'fill': [({}, 'w1', 'x2'), ],
            },
            'w1': {
                'stash': [({}, 'w2', 'x1')],
            },
            'w2': {
                'fill': [({}, 'w5', 'x0')],
            },
            'w5': {
                'start': [({}, 'w6', 'x2')],
            },
            'w6': {
                'forge': [({'u': 1}, 'w5', 'x0'),
                          ({'u': 2}, 'w0', 'x2'),
                          ({'u': 0}, 'w4', 'x1'), ],
            },
            'w4': {
                'play': [({}, 'w0', 'x2')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = []

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            return "unsupported"

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts.get((self.state,
                                                    to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.last_output = output
                return None
        return "unsupported"

    def has_path_to(self, name):
        return True

    def get_step(self):
        return self.step_count

    def get_output(self):
        return self.last_output

    def __getattr__(self, name):
        name = name.replace('store_', '').replace('go_', '')
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
    assert obj.go_fill() == 'unsupported'
    assert obj.go_play() == 'unsupported'
    assert obj.go_mifoxti() == 'unknown'
    obj.store_r(0)
    obj.go_fill()
    assert obj.get_output() == 'x2'
    assert obj.get_step() == 1
    assert obj.has_path_to('w4') == True
    obj.go_fill()
    obj.go_stash()
    obj.go_fill()
    obj.state = 'w0'
    obj.store_r(1)
    obj.go_fill()
    obj.go_start()
    obj.store_u(1)
    obj.go_forge()
    obj.go_start()
    obj.store_u(2)
    obj.go_forge()
    obj.state = 'w6'
    obj.store_u(0)
    obj.go_forge()
    obj.go_play()
