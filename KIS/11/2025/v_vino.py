class MealyAutomat:
    def __init__(self):
        self.state = 'H4'

        self.conditional_transitions = {
            'H4': {
                'show': [({}, 'H1', 'V1')]
            },
            'H1': {
                'speed': [({}, 'H5', 'V0')],
                'show': [({}, 'H0', 'V1')],
            },
            'H5': {
                'march': [({}, 'H0', 'V1')],
            },
            'H0': {
                'tag': [({'y': 0}, 'H2', 'V0'),
                        ({'y': 1}, 'H1', 'V0'),
                        ({'y': 2}, 'H3', 'V0'), ],
            },
            'H2': {
                'march': [({}, 'H3', 'V0')], },
            'H3': {
                'show': [({}, 'H5', 'V0')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.executed_methods = []

    def has_max_out_edges(self):
        return True if self.state == 'H0' else False

    def let_var(self, key, value):
        self.vars[key] = value

    def has_path_to(self, to_state):
        return True if to_state != 'H4' else False

    def seen_method(self, method):
        return self.executed_methods.count(method)

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def go(self, command):
        if not self._trigger_exists(command):
            return 'unknown'

        current_transitions = self.conditional_transitions.get(self.state, {})
        if command not in current_transitions:
            return 'unsupported'

        transitions = current_transitions[command]

        for conds, next_state, output in transitions:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, next_state)] = (
                        self.transition_counts.get((self.state,
                                                    next_state), 0) + 1
                )
                self.state = next_state
                self.step_count += 1
                self.executed_methods.append(command)
                return output
        return 'unsupported'


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.go('show') == 'V1'
    assert obj.go('speed') == 'V0'
    assert obj.go('march') == 'V1'
    assert obj.go('tag') == 'unsupported'
    assert obj.go('speed') == 'unsupported'
    assert obj.go('none') == 'unknown'
    obj.let_var('y', 1)
    assert obj.go('tag') == 'V0'
    assert obj.go('show') == 'V1'
    obj.let_var('y', 0)
    assert obj.go('tag') == 'V0'
    assert obj.go('march') == 'V0'
    assert obj.go('show') == 'V0'
    assert obj.go('march') == 'V1'
    obj.let_var('y', 2)
    assert obj.go('tag') == 'V0'
    assert obj.seen_method('tag') == 3
    assert obj.has_max_out_edges() is False
    assert obj.has_path_to('H1') is True
