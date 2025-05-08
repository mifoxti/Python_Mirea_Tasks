class MealyAutomat:
    def __init__(self):
        self.state = 'V4'

        self.conditional_transitions = {
            'V4': {
                'place': [({}, 'V3', 'T1')]
            },
            'V3': {
                'code': [({}, 'V5', 'T0')],
                'post': [({'h': 1}, 'V4', 'T0'),
                         ({'h': 0}, 'V7', 'T0')],
            },
            'V7': {
                'fetch': [({}, 'V1', 'T0')],
            },
            'V1': {
                'align': [({}, 'V0', 'T1')],
                'code': [({}, 'V2', 'T1')],
            },
            'V0': {
                'align': [({}, 'V7', 'T1')],
            },
            'V2': {
                'code': [({}, 'V3', 'T1')],
                'click': [({}, 'V6', 'T0')],
            },
            'V5': {
                'place': [({'e': 0}, 'V5', 'T0'),
                          ({'e': 1}, 'V0', 'T0')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = []

    def go(self, command):
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
                self.executed_methods.append(command)
                self.last_output = output
                return output
        return 'unsupported'

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in self.conditional_transitions.values())

    def has_max_out_edges(self):
        return False if self.state != 'V3' else True

    def seen_edge(self, from_state, to_state):
        return True if self.transition_counts.get((from_state,
                                                   to_state), 0) else False

    def __getattr__(self, name):
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        return lambda *args, **kwargs: self.go(name)


def main():
    return MealyAutomat()


def test():
    obj = main()
    #
    # obj = main()
    # print(obj.go('mix'))
    # print(obj.e(1))
    # print(obj.seen_edge('V4', 'V3'))
    # print(obj.go('place'))
    # print(obj.go('code'))
    # print(obj.go('place'))
    # print(obj.has_max_out_edges())
    # print(obj.seen_edge('V0', 'V7'))
    # print(obj.go('check'))
    # print(obj.go('align'))
    # print(obj.go('fetch'))
    # print(obj.go('glare'))
    # print(obj.seen_edge('V7', 'V1'))
    # print(obj.has_max_out_edges())
    # print(obj.go('code'))
    # print(obj.go('click'))

    assert obj.state == 'V4'
    assert obj.go('post') == 'unsupported'
    assert obj.go('none') == 'unknown'
    obj.bebra()
    assert obj.has_max_out_edges() is False
    assert obj.go('place') == 'T1'
    assert obj.go('post') == 'unsupported'
    obj.h(1)
    assert obj.go('post') == 'T0'
    obj.state = 'V3'
    obj.h(0)
    assert obj.go('post') == 'T0'
    assert obj.state == 'V7'
    assert obj.go('fetch') == 'T0'
    assert obj.go('align') == 'T1'
    assert obj.go('align') == 'T1'
    obj.state = 'V3'
    assert obj.go('code') == 'T0'
    obj.e(0)
    assert obj.go('place') == 'T0'
    obj.e(1)
    assert obj.go('place') == 'T0'
    obj.state = 'V1'
    assert obj.go('code') == 'T1'
    assert obj.go('code') == 'T1'
    obj.state = 'V2'
    assert obj.go('click') == 'T0'
    assert obj.state == 'V6'
    assert obj.seen_edge('V2', 'V6')
