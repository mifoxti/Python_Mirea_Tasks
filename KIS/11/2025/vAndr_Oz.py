class FSMError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'A3'

        self.conditional_transitions = {
            'A3': {
                'copy': [({}, 'A5', 'e1')]
            },
            'A5': {
                'open': [({}, 'A4', 'e0')],
            },
            'A4': {
                'align': [({}, 'A0', 'e1')],
            },
            'A0': {
                'copy': [({}, 'A0', 'e0')],
                'open': [({}, 'A6', 'e1')],
                'align': [({}, 'A2', 'e2')],
            },
            'A2': {
                'open': [({}, 'A6', 'e2')],
            },
            'A6': {
                'lower': [({}, 'A1', 'e3')],
            },
            'A1': {
                'copy': [({}, 'A2', 'e3')],
                'code': [({}, 'A4', 'e3')],
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
                   for transitions in self.conditional_transitions.values())

    def has_max_in_edges(self):
        return False if self.state not in ['A4', 'A0', 'A2',
                                           'A6'] else True

    def seen_edge(self, from_state, to_state):
        return (from_state, to_state) in self.transition_counts

    def go(self, command):
        if not self._trigger_exists(command):
            raise FSMError('unknown')

        current_transitions = self.conditional_transitions.get(self.state, {})
        if command not in current_transitions:
            raise FSMError('unsupported')

        transitions = current_transitions[command]

        for conds, next_state, output in transitions:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, next_state)] = (
                        self.transition_counts.get((self.state,
                                                    next_state), 0) + 1
                )
                self.state = next_state
                self.step_count += 1
                self.executed_methods.add(command)
                self.last_output = output
                return output
        raise FSMError('unsupported')


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
        assert output is None


def main():
    return MealyAutomat()


def test():
    obj = main()
    raises(lambda: obj.go('open'), FSMError)
    raises(lambda: obj.go('none'), FSMError)
    assert obj.go('copy') == 'e1'
    assert obj.go('open') == 'e0'
    assert obj.go('align') == 'e1'
    assert obj.go('copy') == 'e0'
    assert obj.go('align') == 'e2'
    assert obj.go('open') == 'e2'
    obj.state = 'A0'
    assert obj.go('open') == 'e1'
    assert obj.go('lower') == 'e3'
    assert obj.go('copy') == 'e3'
    assert obj.has_max_in_edges() is True
    assert obj.seen_edge('A1', 'A2') is True
    obj.state = 'A1'
    assert obj.go('code') == 'e3'
    obj.state = 'test'
    raises(lambda: obj.go('debug'), FSMError)
