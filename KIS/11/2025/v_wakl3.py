class MealyAutomat:
    def __init__(self):
        self.state = 'D3'

        self.conditional_transitions = {
            'D3': {
                'march': [({}, 'D2', 'g2')],
            },
            'D2': {
                'patch': [({}, 'D2', 'g2')],
                'walk': [({}, 'D7', 'g3')],
            },
            'D7': {
                'march': [({}, 'D0', 'g1')],
                'patch': [({}, 'D1', 'g3')],
            },
            'D0': {
                'march': [({'y': 0}, 'D1', 'g2'),
                          ({'y': 1}, 'D5', 'g0'), ],
            },
            'D1': {
                'herd': [({}, 'D5', 'g1'), ],
            },
            'D5': {
                'herd': [({}, 'D0', 'g3'), ],
                'patch': [({}, 'D2', 'g3'), ],
                'march': [({}, 'D6', 'g0'), ],
            },
            'D6': {
                'patch': [({}, 'D4', 'g2')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['D3']
        self.executed_methods = []

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
                self.executed_methods.append(name)
                self.last_output = output
                self.executed_states.append(to_state)
                return output
        return "unsupported"

    def store_var(self, name, value):
        self.vars[name] = value

    def seen_method(self, method):
        return self.executed_methods.count(method)

    def get_step(self):
        return self.step_count

    def seen_state(self, state_name):
        return self.executed_states.count(state_name)

    def __getattr__(self, name):
        name = name.replace('move_', '')
        if not self._trigger_exists(name):
            return lambda: "unknown"
        return lambda: (self._try_apply_trigger(name) or None)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.move_march() == "g2"
    assert obj.get_step() == 1
    assert obj.seen_method('march') == 1
    assert obj.seen_state('D3') == 1
    assert obj.move_patch() == "g2"
    assert obj.move_walk() == "g3"
    assert obj.move_march() == "g1"
    assert obj.move_march() == "unsupported"
    assert obj.move_herd() == "unsupported"
    assert obj.move_none() == "unknown"
    obj.store_var("y", 0)
    assert obj.march() == "g2"
    assert obj.herd() == "g1"
    assert obj.herd() == "g3"
    obj.store_var("y", 1)
    assert obj.march() == "g0"
    assert obj.patch() == "g3"
    obj.walk()
    assert obj.patch() == "g3"
    obj.herd()
    assert obj.march() == "g0"
    assert obj.patch() == "g2"
