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

def emit_char(code):
    print(chr(code), end='')

def disasm(bytecode):
    result_string = []
    scope = {}  # Создаем пустое пространство имен scope

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

        elif operation == 2:  # call
            result_string.append(OP_NAMES[operation])

        elif operation == 3:  # is
            result_string.append(OP_NAMES[operation])

        elif operation == 4:  # to
            # Значение для локальной переменной снимается с вершины стека и записывается в scope
            value = result_string.pop()
            variable = result_string.pop()
            scope[variable] = value

        elif operation == 5:  # exit
            break

    return result_string, scope

bytecode = [31, 256, 129, 5, 8, 4, 16, 12, 24, 20, 2, 121, 26, 10, 121, 26, 18, 121, 26, 5,
            32, 4, 40, 12, 34, 2, 121, 26, 10, 121, 26, 5, 0, 27, 48, 4, 24, 35, 152, 43,
            42, 2, 121, 26, 5]

result, scope = disasm(bytecode)
print(" ".join(map(str, result)))
print("Scope:", scope)
