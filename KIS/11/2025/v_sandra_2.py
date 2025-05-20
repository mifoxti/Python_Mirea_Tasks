class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'k4'

        self.conditional_transitions = {
            'k4': {
                'throw': [({'v': 0}, 'k2', 'Q4'),
                          ({'v': 1}, 'k0', 'Q1'), ],
            },
            'k0': {
                'amble': [({}, 'k0', 'Q4'), ],
                'melt': [({}, 'k1', 'Q1'), ],
            },
            'k1': {
                'peek': [({}, 'k2', 'Q0')],
            },
            'k2': {
                'wreck': [({}, 'k5', 'Q4'), ],
            },
            'k5': {
                'amble': [({'h': 1}, 'k2', 'Q4'),
                          ({'h': 0}, 'k3', 'Q0'), ],
            },
            'k3': {
                'pose': [({}, 'k5', 'Q3')],
            },
        }
        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.executed_methods = set()

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            raise MealyError('unsupported')

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts.get((self.state,
                                                    to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.executed_methods.add(name)
                return output

        raise MealyError('unsupported')

    def __getattr__(self, name):
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        if not self._trigger_exists(name):
            raise MealyError('unknown')
        return lambda: (self._try_apply_trigger(name) or None)

    def has_path_to(self, to_state):
        paths = {
            'k4': ['k0', 'k1', 'k2', 'k5', 'k3'],
            'k0': ['k0', 'k1', 'k2', 'k3', 'k5'],
            'k1': ['k2', 'k3', 'k5'],
            'k2': ['k2', 'k3', 'k5'],
            'k5': ['k2', 'k3', 'k5'],
            'k3': ['k2', 'k3', 'k5'],
        }
        return True if to_state in paths[self.state] else False

    def has_max_out_edges(self):
        return True if self.state in ['k4', 'k0', 'k5'] else False


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
    raises(lambda: obj.throw(), MealyError)
    raises(lambda: obj.amble(), MealyError)
    raises(lambda: obj.none(), MealyError)
    assert obj.v(1) is None
    assert obj.throw() == 'Q1'
    assert obj.has_path_to('k2')
    assert obj.has_max_out_edges() is True
    assert obj.amble() == 'Q4'
    assert obj.melt() == 'Q1'
    assert obj.peek() == 'Q0'
    assert obj.wreck() == 'Q4'
    assert obj.h(0) is None
    assert obj.amble() == 'Q0'
    assert obj.pose() == 'Q3'
    assert obj.h(1) is None
    assert obj.amble() == 'Q4'
    obj.state = 'k4'
    assert obj.v(0) is None
    assert obj.throw() == 'Q4'
