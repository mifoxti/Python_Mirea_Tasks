class MealyAutomat:
    def __init__(self):
        self.state = 'K1'

        self.conditional_transitions = {
            'K1': {
                'carve': [({}, 'K3', 'G2'), ],
            },
            'K3': {
                'close': [({'d': 0}, 'H4', 'M4'),]
            },
            'K4': {
                'close': [({'m': 0}, 'K0', 'G4'),
                         ({'m': 1}, 'K6', 'G5'),],
                'turn': [({}, 'K2', 'G2')]
            },
            'K2': {
                'fill': [({}, 'K1', 'G6')],
                'crack': [({}, 'K0', 'G4')],
            },
            'K0': {
                'crack': [({}, 'K6', 'G5')],
            },
            'K6': {
                'clear': [({}, 'H0', 'M1')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['H3']
        self.executed_methods = set()

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def get_step(self):
        return self.step_count

    def has_max_in_edges(self):
        return False if self.state not in ['K0'] else True

    def select(self, command):
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
                self.executed_methods.add(command)
                self.last_output = output
                return None
        return 'unsupported'

    def set_var(self, var, value):
        self.vars[var] = value

    def seen_edge(self, from_state, to_state):
        return (from_state, to_state) in self.transition_counts

    def seen_method(self, method_name):
        return method_name in self.executed_methods

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
