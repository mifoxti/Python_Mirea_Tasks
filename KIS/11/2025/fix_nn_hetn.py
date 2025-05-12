class MealyAutomat:
    def __init__(self):
        self.state = 'd2'

        self.conditional_transitions = {
            'd2': {
                'crash': [({}, 'd3', 'e0')],
            },
            'd3': {
                'play': [({'n': 0}, 'd3', 'e2'),
                         ({'n': 1}, 'd7', 'e1'), ],
            },
            'd7': {
                'link': [({}, 'd3', 'e0')],
                'hurry': [({}, 'd5', 'e1'), ],
            },
            'd5': {
                'shade': [({}, 'd5', 'e1')],
                'crash': [({}, 'd0', 'e1'), ],
            },
            'd0': {
                'glare': [({}, 'd5', 'e0')],
                'play': [({}, 'd6', 'e1'), ],
            },
            'd6': {
                'shade': [({}, 'd1', 'e0')],
            },
            'd1': {
                'hurry': [({'v': 0}, 'd1', 'e1'),
                          ({'v': 1}, 'd4', 'e2'), ],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['d2']

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
                self.executed_states.append(to_state)
                return output
        return "unsupported"

    def has_path_to(self, target_state):
        paths = {
            'd2': ['d3', 'd7', 'd5', 'd0', 'd6', 'd1', 'd4'],
            'd3': ['d3', 'd7', 'd5', 'd0', 'd6', 'd1', 'd4'],
            'd7': ['d3', 'd7', 'd5', 'd0', 'd6', 'd1', 'd4'],
            'd5': ['d5', 'd0', 'd6', 'd1', 'd4'],
            'd0': ['d5', 'd0', 'd6', 'd1', 'd4'],
            'd6': ['d1', 'd4'],
            'd1': ['d1', 'd4'],
            'd4': [],
        }
        return target_state in paths[self.state]

    def seen_state(self, state_name):
        return self.executed_states.count(state_name)

    def seen_edge(self, from_state, to_state):
        return self.transition_counts.get((from_state, to_state), 0)

    def __getattr__(self, name):
        name = name.replace('store_', '')
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
    assert obj.seen_state('d2') == 1
    assert obj.crash() == 'e0'
    assert obj.play() == 'unsupported'
    assert obj.link() == 'unsupported'
    assert obj.none() == 'unknown'
    assert obj.store_n(0) is None
    assert obj.play() == 'e2'
    assert obj.store_n(1) is None
    assert obj.play() == 'e1'
    assert obj.link() == 'e0'
    assert obj.play() == 'e1'
    assert obj.hurry() == 'e1'
    assert obj.shade() == 'e1'
    assert obj.crash() == 'e1'
    assert obj.glare() == 'e0'
    assert obj.crash() == 'e1'
    assert obj.play() == 'e1'
    assert obj.shade() == 'e0'
    assert obj.store_v(0) is None
    assert obj.hurry() == 'e1'
    assert obj.store_v(1) is None
    assert obj.hurry() == 'e2'
    assert obj.state == 'd4'
    assert obj.seen_edge('d1', 'd4') == 1
    assert obj.has_path_to('d7') is False
    assert obj.seen_state('d2') == 1
