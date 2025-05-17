class MealyAutomat:
    def __init__(self):
        self.state = 'N7'

        self.conditional_transitions = {
            'N7': {
                'crawl': [({}, 'N4', 'X0')],
                'sway': [({"p": 0}, 'N0', 'X1'),
                         ({"p": 1}, 'N2', 'X2')]
            },
            'N4': {
                'lower': [({}, 'N2', 'X2')],
            },
            'N2': {
                'loop': [({}, 'N1', 'X2')],
            },
            'N1': {
                'sway': [({}, 'N2', 'X2')],
                'loop': [({}, 'N3', 'X0')],
            },
            'N3': {
                'sway': [({}, 'N6', 'X1'), ],
            },
            'N6': {
                'melt': [({}, 'N0', 'X1'), ],
            },
            'N0': {
                'warp': [({}, 'N5', 'X2')],
                'loop': [({}, 'N6', 'X1')],
            },
            'N5': {
                'lower': [({}, 'N6', 'X1')],
            }
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = []

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in self.conditional_transitions.values())

    def run(self, command):
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
                self.last_output = output
                return None
        return 'unsupported'

    def has_max_out_edges(self):
        return True if self.state == 'N7' else False

    def assign_var(self, name, value):
        self.vars[name] = value

    def seen_method(self, method):
        return self.executed_methods.count(method)

    def get_output(self):
        return self.last_output


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.run('sway') == "unsupported"
    assert obj.run('melt') == "unsupported"
    assert obj.run('bebra') == "unknown"
    assert obj.has_max_out_edges() is True
    obj.run('crawl')
    assert obj.seen_method('crawl') == 1
    assert obj.get_output() == "X0"
    assert obj.state == 'N4'
    obj.run('lower')
    obj.run('loop')
    obj.run('sway')
    obj.run('loop')
    obj.run('loop')
    obj.run('sway')
    obj.run('melt')
    obj.run('loop')
    obj.run('melt')
    obj.run('warp')
    obj.run('lower')
    obj.state = 'N7'
    obj.assign_var('p', 0)
    obj.run('sway')
    obj.state = 'N7'
    obj.assign_var('p', 1)
    obj.run('sway')
