class MealyAutomat:
    def __init__(self):
        self.state = 'W3'

        self.conditional_transitions = {
            'W3': {
                'start': [({}, 'W6', 'G6')],
                'crash': [({}, 'W4', 'G0')],
            },
            'W6': {
                'trash': [({}, 'W1', 'G0'), ],
                'start': [({}, 'W0', 'G1')],
            },
            'W1': {
                'start': [({}, 'W5', 'G5')],
            },
            'W5': {
                'crash': [({}, 'W2', 'G6')],
            },
            'W2': {
                'build': [({}, 'W5', 'G1')],
                'sway': [({}, 'W4', 'G4')],
            },
            'W4': {
                'start': [({}, 'W0', 'G1')],
            },
            'W0': {
                'crash': [({}, 'W6', 'G6')],
            },
            'test': {
                'debug': [({'i': 1}, 'none', 'none')],
            }
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
                return output
        return "unsupported"

    def has_max_out_edges(self):
        return False if self.state not in ["W6", "W2", "W3"] \
            else True

    def seen_edge(self, from_state, to_state):
        return self.transition_counts.get((from_state, to_state), 0)

    def __getattr__(self, name):
        if not self._trigger_exists(name):
            return lambda: "unknown"
        return lambda: (self._try_apply_trigger(name) or None)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.has_max_out_edges()
    assert obj.state == 'W3'
    assert obj.start() == 'G6'
    assert obj.trash() == 'G0'
    assert obj.start() == 'G5'
    assert obj.crash() == 'G6'
    assert obj.build() == 'G1'
    obj.state = 'W2'
    assert obj.sway() == 'G4'
    assert obj.start() == 'G1'
    assert obj.crash() == 'G6'
    assert obj.start() == 'G1'
    assert obj.seen_edge('W6', 'W0')
    assert obj.start() == 'unsupported'
    assert obj.none() == 'unknown'
    obj.state = 'test'
    assert obj.debug() == 'unsupported'
