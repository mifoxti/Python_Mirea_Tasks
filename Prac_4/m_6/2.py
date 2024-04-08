OP_NAMES = {0: 'push', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}

LIB = [
    '+',
    '-',
    '*',
    '/',
    '%',
    '&',
    '|',
    '^',
    '<',
    '>',
    '=',
    '<<',
    '>>',
    'if',
    'for',
    '.',
    'emit',
    '?',
    'array',
    '@',
    '!'
]


def disasm(bytecode):

    result_string = []

    for ip in range(len(bytecode)):

        opcode = bytecode[ip]
        mask_op = 0b111

        operation = opcode & mask_op
        value = opcode >> 3

        if operation == 0 and value == 0:
            pass

        elif operation == 0:
            result_string.append(value)

        elif operation == 1:
            result_string.append(LIB[value])

        elif operation == 5:
            break
    return result_string


bytecode = [0, 16, 16, 1, 121, 5]
print(disasm(bytecode))
