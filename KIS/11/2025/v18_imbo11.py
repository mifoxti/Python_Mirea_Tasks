class MooreException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'p4'

        self.conditional_transitions = {
            'p4': {
                'trim': [({}, 'p5', 'A1')],
            },
            'p5': {
                'sort': [({}, 'p4', 'A2')],
                'sit': [({}, 'p2', 'A0')],
            },
            'p2': {
                'coat': [({}, 'p2', 'A0')],
                'crawl': [({}, 'p6', 'A1')],
            },
            'p6': {
                'trim': [({}, 'p3', 'A0')],
            },
            'p3': {
                'sit': [({}, 'p0', 'A0')],
            },
            'p0': {
                'trim': [({}, 'p6', 'A1')],
                'sort': [({}, 'p4', 'A2')],
                'sit': [({}, 'p7', 'A1')],
            },
            'p7': {
                'crawl': [({}, 'p1', 'A2')],
            },
            'p1': {
                'crawl': [({}, 'p4', 'A2')],
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
        self.method_call_counts = {}

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
                self.executed_methods.add(name)
                self.method_call_counts[name] = (
                        self.method_call_counts.get(name, 0) + 1)
                return None
        raise MooreException("unsupported")

    def has_max_in_edges(self):
        return self.state == 'p4'

    def get_output(self):
        return self.last_output

    def seen_method(self, method_name):
        return self.method_call_counts.get(method_name, 0)

    def __getattr__(self, name):
        name = name.replace('move_', '')
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
    raises(lambda: obj.move_sort(), MooreException)
    raises(lambda: obj.move_soprano(), MooreException)
    assert obj.has_max_in_edges() is True
    obj.move_trim()
    assert obj.get_output() == 'A1'
    obj.sit()
    assert obj.get_output() == 'A0'
    obj.coat()
    obj.crawl()
    obj.trim()
    obj.sit()
    obj.trim()
    obj.state = 'p0'
    obj.sort()
    obj.state = 'p0'
    obj.sit()
    obj.crawl()
    obj.crawl()
    obj.state = 'test'
    assert obj.seen_method('sit') == 3
    raises(lambda: obj.debug(), MooreException)
