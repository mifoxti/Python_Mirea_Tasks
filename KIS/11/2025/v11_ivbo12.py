class StateMachineException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'r1'

        self.conditional_transitions = {
            'r1': {
                'stop': [({'a': 1}, 'r1', 'T1'),
                         ({'a': 0}, 'r2', 'T0'), ],
                'coat': [({}, 'r5', 'T2')]
            },
            'r2': {
                'align': [({}, 'r0', 'T1')],
            },
            'r0': {
                'bend': [({'h': 0}, 'r3', 'T2'),
                         ({'h': 1}, 'r4', 'T0'), ],
            },
            'r3': {
                'coat': [({}, 'r4', 'T0')],
            },
            'r4': {
                'stop': [({'e': 1}, 'r3', 'T2'),
                         ({'e': 0}, 'r5', 'T2'), ],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = []

    def move(self, command):
        if not self._trigger_exists(command):
            raise StateMachineException('unknown')

        current_transitions = self.conditional_transitions.get(self.state, {})
        if command not in current_transitions:
            raise StateMachineException('unsupported')

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
        raise StateMachineException('unsupported')

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in self.conditional_transitions.values())

    def has_max_in_edges(self):
        return False if self.state not in ['r3', 'r4', 'r5'] else True

    def get_step(self):
        return self.step_count

    def get_output(self):
        return self.last_output

    def assign_var(self, name, value):
        self.vars[name] = value

    def seen_method(self, method):
        return method in self.executed_methods


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
    raises(lambda: obj.move('stop'), StateMachineException)
    raises(lambda: obj.move('bend'), StateMachineException)
    raises(lambda: obj.move('cat'), StateMachineException)
    assert obj.has_max_in_edges() is False
    assert obj.get_step() == 0
    assert obj.seen_method('stop') is False
    obj.assign_var('a', 1)
    obj.move('stop')
    assert obj.get_output() == 'T1'
    obj.move('coat')
    obj.state = 'r1'
    obj.assign_var('a', 0)
    obj.move('stop')
    obj.move('align')
    obj.assign_var('h', 0)
    obj.move('bend')
    obj.move('coat')
    obj.assign_var('e', 1)
    obj.move('stop')
    obj.state = 'r4'
    obj.assign_var('e', 0)
    obj.move('stop')
    assert obj.get_output() == 'T2'
    assert obj.state == 'r5'
    obj.state = 'r0'
    obj.assign_var('h', 1)
    obj.move('bend')
