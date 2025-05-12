class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'f3'

        self.conditional_transitions = {
            'f3': {
                'load': [({}, 'f7', 'h0'), ],
            },
            'f7': {
                'drag': [({}, 'f6', 'h2'), ],
            },
            'f6': {
                'post': [({}, 'f0', 'h0')],
            },
            'f0': {
                'drag': [({'z': 0}, 'f6', 'h0'),
                         ({'z': 1}, 'f2', 'h0')],
            },
            'f2': {
                'drag': [({'a': 0}, 'f7', 'h2'),
                         ({'a': 1}, 'f4', 'h2')],
            },
            'f4': {
                'rush': [({}, 'f5', 'h2'), ],
            },
            'f5': {
                'drag': [({'v': 0}, 'f4', 'h4'),
                         ({'v': 1}, 'f1', 'h4'),
                         ({'v': 2}, 'f7', 'h6'), ],
            },
            'f1': {
                'debug': [({}, 'f3', 'h1'), ],
            }
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = ['']
        self.method_call_counts = {}

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            raise MealyError("unsupported")

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts.get((self.state,
                                                    to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.last_output = output
                self.method_call_counts[name] = (
                        self.method_call_counts.get(name, 0) + 1)
                return output
        raise MealyError("unsupported")

    def has_path_to(self, name):
        return True

    def set_var(self, key, value):
        self.vars[key] = value

    def seen_method(self, method_name):
        return self.method_call_counts.get(method_name, 0)

    def has_max_out_edges(self):
        return True if self.state == 'f5' else False

    def __getattr__(self, name):
        name = name.replace('run_', '')
        if not self._trigger_exists(name):
            raise MealyError("unknown")
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
    assert obj.state == 'f3'
    assert obj.run_load() == 'h0'
    assert obj.run_drag() == 'h2'
    assert obj.run_post() == 'h0'
    raises(lambda: obj.run_drag(), MealyError)
    raises(lambda: obj.run_post(), MealyError)
    raises(lambda: obj.run_point(), MealyError)
    obj.set_var('z', 0)
    obj.state = 'f0'
    obj.set_var('z', 1)
    assert obj.run_drag() == 'h0'
    obj.set_var('a', 0)
    assert obj.run_drag() == 'h2'
    obj.state = 'f2'
    obj.set_var('a', 1)
    assert obj.run_drag() == 'h2'
    assert obj.run_rush() == 'h2'
    assert obj.has_max_out_edges() is True
    assert obj.seen_method('drag') == 4
    assert obj.has_path_to('f3') == True
    assert obj.state == 'f5'
    obj.set_var('v', 0)
    assert obj.run_drag() == 'h4'
    obj.state = 'f5'
    obj.set_var('v', 2)
    assert obj.run_drag() == 'h6'
    obj.state = 'f5'
    obj.set_var('v', 1)
    assert obj.run_drag() == 'h4'
    assert obj.run_debug() == 'h1'
