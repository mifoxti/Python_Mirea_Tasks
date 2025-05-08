class StateMachineException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 's3'

        self.conditional_transitions = {
            's3': {
                'apply': [({}, 's0', 'u4')]
            },
            's0': {
                'crawl': [({}, 's4', 'u0')],
            },
            's4': {
                'crawl': [({}, 's0', 'u4')],
                'amble': [({'d': 1}, 's5', 'u4'),
                          ({'d': 0}, 's2', 'u4')],
            },
            's5': {
                'align': [({'t': 1}, 's5', 'u4'),
                          ({'t': 0}, 's1', 'u0')],
                'apply': [({}, 's2', 'u4')],
            },
            's2': {
                'amble': [({}, 's5', 'u4')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_state = None
        self.executed_methods = set()

    def has_path_to(self, target_state):
        paths = {
            's3': ['s0', 's4', 's5', 's2', 's1'],
            's0': ['s0', 's4', 's5', 's2', 's1'],
            's4': ['s0', 's4', 's5', 's2', 's1'],
            's5': ['s5', 's2', 's1'],
            's2': ['s2', 's5', 's1'],
            's1': [],
        }
        return target_state in paths[self.state]

    def get_step(self):
        return self.step_count

    def get_output(self):
        return self.last_state

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = (
            self.conditional_transitions.get(self.state, {})
        )
        if name not in current_transitions:
            raise StateMachineException("unsupported")

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts
                        .get((self.state, to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.executed_methods.add(name)
                self.last_state = output
                return None
        raise StateMachineException("unsupported")

    def __getattr__(self, name):
        name = name.lstrip('go_')
        name = name.replace('store_', '')
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        if not self._trigger_exists(name):
            raise StateMachineException("unknown")
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
    assert obj.state == 's3'
    obj.go_apply()
    assert obj.has_path_to('s1')
    assert obj.get_output() == 'u4'
    obj.go_crawl()
    obj.go_crawl()
    obj.go_crawl()
    assert obj.state == 's4'
    raises(lambda: obj.go_amble(), StateMachineException)
    obj.store_d(1)
    obj.go_amble()
    obj.state = 's4'
    obj.store_d(0)
    obj.go_amble()
    obj.go_amble()
    obj.go_apply()
    obj.go_amble()
    assert obj.state == 's5'
    obj.store_t(1)
    obj.go_align()
    obj.store_t(0)
    obj.go_align()
    obj.get_step()
    raises(lambda: obj.go_amble(), StateMachineException)
    raises(lambda: obj.go_pivo(), StateMachineException)
