class FSMException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'H3'

        self.conditional_transitions = {
            'H3': {
                'sweep': [({}, 'H4', 'M1'), ],
                'tweak': [({}, 'H2', 'M4'), ],
            },
            'H4': {
                'sweep': [({'d': 0}, 'H4', 'M4'),
                          ({'d': 1}, 'H2', 'M1'), ],
            },
            'H2': {
                'post': [({'y': 0}, 'H6', 'M4'),
                         ({'y': 1}, 'H4', 'M2'),
                         ({'y': 2}, 'H2', 'M0'), ],
            },
            'H6': {
                'post': [({}, 'H1', 'M4')],
            },
            'H1': {
                'scale': [({}, 'H5', 'M1')],
            },
            'H5': {
                'tweak': [({}, 'H0', 'M1')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['H3']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            raise FSMException("unsupported")

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
        raise FSMException("unsupported")

    def get_step(self):
        return self.step_count

    def has_max_in_edges(self):
        return False if self.state not in ['H4', 'H2'] else True

    def __getattr__(self, name):
        name = name.replace('let_', '')
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        if not self._trigger_exists(name):
            raise FSMException("unknown")
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
    assert obj.sweep() == 'M1'
    raises(lambda: obj.sweep(), FSMException)
    raises(lambda: obj.post(), FSMException)
    raises(lambda: obj.none(), FSMException)
    obj.let_d(0)
    assert obj.sweep() == 'M4'
    obj.let_d(1)
    assert obj.sweep() == 'M1'
    obj.let_y(1)
    assert obj.post() == 'M2'
    assert obj.sweep() == 'M1'
    obj.let_y(2)
    assert obj.post() == 'M0'
    obj.state = 'H3'
    assert obj.tweak() == 'M4'
    assert obj.has_max_in_edges() is True
    obj.let_y(0)
    assert obj.post() == 'M4'
    assert obj.post() == 'M4'
    assert obj.scale() == 'M1'
    assert obj.tweak() == 'M1'
    assert obj.state == 'H0'
    assert obj.get_step() != 0
