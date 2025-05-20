class MealyAutomat:
    def __init__(self):
        self.state = 's4'

        self.conditional_transitions = {
            's4': {
                'hoard': [({}, 's5', 'u5')],
            },
            's5': {
                'loop': [({}, 's0', 'u5'), ],
            },
            's0': {
                'glare': [({}, 's5', 'u5')],
                'put': [({}, 's3', 'u2')],
                'hoard': [({}, 's2', 'u1')],
            },
            's3': {
                'glare': [({}, 's2', 'u1'), ],
            },
            's2': {
                'put': [({}, 's3', 'u2')],
                'jog': [({}, 's1', 'u4')],
            },
            's1': {
                'jog': [({}, 's0', 'u5'), ],
            },
            'test': {
                'debug': [({'i': 1}, 'none', 'none')],
            }
        }
        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = set()

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            return 'unsupported'

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts.get((self.state,
                                                    to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.executed_methods.add(name)
                self.last_output = output
                return None

        return 'unsupported'

    def __getattr__(self, name):
        name = name.replace('select_', '')
        if not self._trigger_exists(name):
            return lambda: 'unknown'
        return lambda: (self._try_apply_trigger(name) or None)

    def part_of_loop(self):
        return True if self.state != 's4' else False

    def seen_method(self, method):
        return True if method in self.executed_methods else False

    def has_max_in_edges(self):
        return True if self.state in ['s5', 's0', 's3', 's2'] else False

    def get_output(self):
        return self.last_output


def main():
    return MealyAutomat()


def test():
    obj = main()
    obj.hoard()
    assert obj.get_output() == 'u5'
    assert obj.part_of_loop() is True
    assert obj.seen_method('hoard') is True
    assert obj.has_max_in_edges() is True
    obj.loop()
    obj.glare()
    obj.loop()
    obj.put()
    obj.glare()
    obj.put()
    obj.glare()
    obj.jog()
    obj.jog()
    obj.hoard()
    obj.state = 'test'
    assert obj.debug() == 'unsupported'
    assert obj.jog() == 'unsupported'
    assert obj.none() == "unknown"
