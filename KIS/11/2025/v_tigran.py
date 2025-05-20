class MooreError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'A4'

        self.conditional_transitions = {
            'A4': {
                'join': [({}, 'A5', 'R2')]
            },
            'A5': {
                'show': [({}, 'A3', 'R0')],
                'join': [({}, 'A0', 'R2')],
                'add': [({}, 'A4', 'R1')],
            },
            'A3': {
                'shade': [({}, 'A6', 'R2')],
            },
            'A6': {
                'shade': [({}, 'A2', 'R2')],
            },
            'A2': {
                'show': [({}, 'A4', 'R1')],
                'join': [({}, 'A1', 'R0')],
                'split': [({}, 'A0', 'R2')],
            },
            'A0': {
                'shade': [({}, 'A3', 'R0')],
            },
            'A1': {
                'test': [({'none': 1}, 'none', 'none')],
            }
        }
        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = []
        self.executed_states = ['A4']
        self.method_call_counts = {}

    def has_max_in_edges(self):
        return True if self.state in ['A4', 'A3', 'A0'] else False

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def seen_state(self, state_name):
        return state_name in self.executed_states

    def seen_method(self, method_name):
        return self.method_call_counts.get(method_name, 0)

    def get_output(self):
        return self.last_output

    def move(self, command):
        if not self._trigger_exists(command):
            raise MooreError('unknown')

        current_transitions = self.conditional_transitions.get(self.state, {})
        if command not in current_transitions:
            raise MooreError('unsupported')

        transitions = current_transitions[command]

        for conds, next_state, output in transitions:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, next_state)] = (
                        self.transition_counts.get((self.state,
                                                    next_state), 0) + 1
                )
                self.state = next_state
                self.step_count += 1
                self.executed_states.append(next_state)
                self.last_output = output
                self.method_call_counts[command] = (
                        self.method_call_counts.get(command, 0) + 1)
                return None
        raise MooreError('unsupported')


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
    assert obj.move('join') is None
    assert obj.get_output() == 'R2'
    obj.move('add')
    obj.move('join')
    obj.move('show')
    obj.move('shade')
    obj.move('shade')
    obj.move('show')
    obj.state = 'A5'
    obj.move('join')
    obj.move('shade')
    obj.state = 'A2'
    obj.move('join')
    raises(lambda: obj.move('test'), MooreError)
    raises(lambda: obj.move('shade'), MooreError)
    raises(lambda: obj.move('none'), MooreError)
    obj.state = 'A2'
    obj.move('split')
    assert obj.seen_method('shade') == 3
    assert obj.seen_state('A4') is True
    assert obj.has_max_in_edges() is True
