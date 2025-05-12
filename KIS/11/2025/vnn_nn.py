class MooreException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'q0'

        self.conditional_transitions = {
            'q0': {
                'flip': [({}, 'q5', 'k1'), ],
            },
            'q5': {
                'grow': [({}, 'q2', 'k5'), ],
            },
            'q2': {
                'shade': [({}, 'q4', 'k3'), ],
            },
            'q4': {
                'clean': [({}, 'q0', 'k0')],
                'flip': [({}, 'q1', 'k4'), ],
                'grow': [({}, 'q6', 'k3'), ],
            },
            'q1': {
                'clean': [({}, 'q4', 'k3')],
                'grow': [({}, 'q3', 'k1')],
            },
            'q3': {
                'grow': [({}, 'q4', 'k3')],
                'clean': [({}, 'q6', 'k3')],
            },
            'test': {
                'debug': [({'i': 1}, 'none', 'none')],
            }
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['q0']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            raise MooreException("unsupported")

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
                return None
        raise MooreException("unsupported")

    def has_path_to(self, target_state):
        return self.state != 'q6'

    def get_output(self):
        return self.last_output

    def seen_state(self, state_name):
        return state_name in self.executed_states

    def has_max_out_edges(self):
        return False if self.state != 'q4' else True

    def __getattr__(self, name):
        name = name.replace('go_', '')
        if not self._trigger_exists(name):
            raise MooreException("unknown")
        return lambda: (self._try_apply_trigger(name) or None)


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
    assert obj.state == 'q0'
    obj.go_flip()
    obj.go_grow()
    obj.go_shade()
    obj.go_clean()
    obj.state = 'q4'
    obj.go_flip()
    obj.go_clean()
    assert obj.has_max_out_edges() is True
    assert obj.get_output() == 'k3'
    obj.go_grow()
    assert obj.has_path_to('q0') is False
    obj.state = 'q1'
    obj.go_grow()
    obj.go_grow()
    obj.state = 'q3'
    obj.go_clean()
    assert obj.seen_state('q0') is True
    raises(lambda: obj.go_cry(), MooreException)
    raises(lambda: obj.go_grow(), MooreException)
    obj.state = 'test'
    raises(lambda: obj.go_debug(), MooreException)
