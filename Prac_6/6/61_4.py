def markov(input_string, rules):
    tape = list(input_string)
    stack = []

    for symbol in tape:
        symbol_type = determine_symbol_type(symbol)

        rule_found = False
        for rule in rules[symbol_type]:
            if symbol.startswith(rule[0]):
                if len(rule[1]) > 0:
                    stack.append(rule[1])
                if rule[2] == 'pop':
                    if len(stack) > 0 and stack[-1] == rule[1]:
                        stack.pop()
                rule_found = True
                break

        if not rule_found:
            return 'E'

    if len(stack) == 0:
        return 'E'
    else:
        return ''.join(stack)


def determine_symbol_type(symbol):
    if symbol in '()+-*/':
        return 'operator'
    elif symbol.isdigit():
        return 'number'
    elif symbol.isalpha():
        return 'function'
    elif symbol in ' ':
        return 'whitespace'
    else:
        return 'unknown'


syntax_rules = {
    'operator': [
        ('+', '+', 'pop'),
        ('-', '-', 'pop'),
        ('*', '*', 'pop'),
        ('/', '/', 'pop'),
        ('(', '(', 'push'),
        (')', ')', 'pop'),
    ],
    'number': [
        ('0', '0', ''),
        ('1', '1', ''),
        ('2', '2', ''),
        ('3', '3', ''),
        ('4', '4', ''),
        ('5', '5', ''),
        ('6', '6', ''),
        ('7', '7', ''),
        ('8', '8', ''),
        ('9', '9', ''),
    ],
    'function': [
        ('func1', 'func1', ''),
        ('func2', 'func2', ''),
        ('func1(', 'func1(', 'push'),
        ('func2(', 'func2(', 'push'),
        ('func1)', 'func1)', 'pop'),
        ('func2)', 'func2)', 'pop')
    ],
    'whitespace': [
        (' ', ''),
    ],
    'unknown': []
}

print(markov('func1( -12* (1 + 4)) - func2(123 /3)', syntax_rules))  # Вывод: E
print(markov('func1( -12* (1 + 4+)) - (123 /3)', syntax_rules))    # Вывод: E*(E+)E
