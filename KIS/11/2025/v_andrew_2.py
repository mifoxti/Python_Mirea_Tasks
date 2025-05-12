class MealyAutomat:
    def __init__(self):
        self.state = 'r4'

        self.conditional_transitions = {
            'r4': {
                'rig': [({'y': 1}, 'r2', 'n1'),
                        ({'y': 0}, 'r0', 'n1'), ],
                'peep': [({}, 'r3', 'n0'), ]
            },
            'r2': {
                'grow': [({}, 'r3', 'n0'), ],
            },
            'r3': {
                'scan': [({}, 'r0', 'n1'), ],
            },
            'r0': {
                'peep': [({'w': 0}, 'r1', 'n1'),
                         ({'w': 1}, 'r3', 'n0'), ],
                'melt': [({}, 'r5', 'n0'), ],
            },
            'r1': {
                'dash': [({}, 'r5', 'n0')],
                'drag': [({}, 'E4', 't1'), ],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.method_call_counts = {}
        self.executed_states = ['r4']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in self.conditional_transitions.values())

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
                self.executed_states.append(to_state)
                self.method_call_counts[name] = (
                        self.method_call_counts.get(name, 0) + 1)
                return None
        return "unsupported"

    def seen_method(self, method_name):
        return self.method_call_counts.get(method_name, 0)

    def get_output(self):
        return self.last_output

    def part_of_loop(self):
        return True if self.state in ["r3", "r0"] else False

    def __getattr__(self, name):
        name = name.replace('let_', '')
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
    assert obj.rig() == "unsupported"
    assert obj.grow() == "unsupported"
    assert obj.morkov() == "unknown"
    obj.let_y(1)
    obj.rig()
    assert obj.get_output() == "n1"
    obj.grow()
    obj.scan()
    assert obj.part_of_loop() is True
    obj.let_w(1)
    obj.peep()
    obj.state = "r4"
    obj.peep()
    obj.state = "r4"
    obj.let_y(0)
    obj.rig()
    obj.let_w(0)
    obj.peep()
    obj.dash()
    obj.state = 'r0'
    obj.melt()
    assert obj.seen_method('peep') == 3
