class MealyAutomat:
    def __init__(self):
        self.state = 'X3'

        self.conditional_transitions = {
            'X3': {
                'unite': [({}, 'X5', 'W1')]
            },
            'X5': {
                'fork': [({}, 'X1', 'W2')],
                'glare': [({}, 'X2', 'W1')],
            },
            'X2': {
                'bolt': [({}, 'X7', 'W2')],
            },
            'X7': {
                'unite': [({'v': 0}, 'X5', 'W0'),
                          ({'v': 1}, 'X1', 'W2')],
            },
            'X1': {
                'fork': [
                    ({'a': 1}, 'X6', 'W2'),
                    ({'a': 2}, 'X4', 'W0'),
                    ({'a': 0}, 'X3', 'W0'),
                ],
            },
            'X6': {
                'mute': [({}, 'X0', 'W1')],
            },
            'X0': {
                'mute': [({}, 'X6', 'W2')],
                'glare': [({}, 'X4', 'W2')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0

    def has_max_out_edges(self):
        out_counts = {}
        for state, transitions in self.conditional_transitions.items():
            count = 0
            for action, variants in transitions.items():
                count += len(variants)
            out_counts[state] = count

        max_out = max(out_counts.values(), default=0)
        return out_counts.get(self.state, 0) == max_out

    def get_step(self):
        return self.step_count

    def let_var(self, key, value):
        self.vars[key] = value

    def _trigger_exists(self, name):
        """Проверяет, существует ли триггер в любом состоянии автомата."""
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        """Пытается применить триггер в текущем состоянии."""
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
                return output
        return 'unsupported'

    def __getattr__(self, name):
        if not self._trigger_exists(name):
            return lambda: 'unknown'
        return lambda: self._try_apply_trigger(name)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.has_max_out_edges() is False
    assert obj.state == 'X3'
    assert obj.unite() == 'W1'
    assert obj.state == 'X5'
    assert obj.glare() == 'W1'
    assert obj.state == 'X2'
    assert obj.bolt() == 'W2'
    assert obj.state == 'X7'
    obj.let_var('v', 0)
    assert obj.unite() == 'W0'
    assert obj.fork() == 'W2'
    assert obj.state == 'X1'
    obj.state = 'X7'
    obj.let_var('v', 1)
    assert obj.unite() == 'W2'
    assert obj.has_max_out_edges() is True
    obj.let_var('a', 0)
    assert obj.fork() == 'W0'
    obj.state = 'X1'
    obj.unite()
    obj.let_var('a', 1)
    assert obj.fork() == 'W2'
    assert obj.state == 'X6'
    assert obj.mute() == 'W1'
    assert obj.state == 'X0'
    assert obj.mute() == 'W2'
    obj.state = 'X0'
    assert obj.glare() == 'W2'
    assert obj.state == 'X4'
    obj.state = 'X1'
    obj.let_var('a', 2)
    assert obj.fork() == 'W0'
    obj.get_step()
    obj.gone()
    obj.state = 'X7'
    obj.vars.clear()
    obj.unite()
