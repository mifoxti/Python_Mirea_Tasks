class MealyAutomat:
    def __init__(self):
        self.state = 'C3'

        self.conditional_transitions = {
            'C3': {
                'visit': [({}, 'C2', 'p1')],
                'widen': [({}, 'C0', 'p1')],
            },
            'C2': {
                'merge': [({}, 'C5', 'p0'), ],
            },
            'C5': {
                'build': [({}, 'C2', 'p3'), ],
                'slur': [({}, 'C0', 'p5')],
            },
            'C0': {
                'build': [({}, 'C4', 'p1')],
            },
            'C4': {
                'widen': [({'z': 1}, 'C3', 'p0'),
                          ({'z': 0}, 'C1', 'p0'), ],
            },
            'C1': {
                'widen': [({}, 'C0', 'p0')],
            },
        }
        self.transition_counts = {}
        self.vars = {}
        self.executed_methods = set()
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['C3']

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

    def part_of_loop(self):
        return True

    def has_max_out_edges(self):
        return True if self.state in ['C3', 'C5', 'C4'] else False

    def has_max_in_edges(self):
        return True if self.state == 'C0' else False

    def __getattr__(self, name):
        name = name.replace('assign_', '')
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
    assert obj.has_max_in_edges() is False
    assert obj.rev() == 'unknown'
    assert obj.has_max_out_edges() is True
    assert obj.merge() == 'unsupported'
    assert obj.visit() == 'p1'
    assert obj.merge() == 'p0'
    assert obj.link() == 'unknown'
    assert obj.slur() == 'p5'
    assert obj.build() == 'p1'
    assert obj.part_of_loop() is True
    assert obj.has_max_out_edges() is True
    assert obj.widen() == 'unsupported'
    assert obj.assign_z(1) is None
    assert obj.widen() == 'p0'
    assert obj.widen() == 'p1'
