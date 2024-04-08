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
            result_string.append(OP_NAMES[operation])

        elif operation == 5:  # exit
            break

    return result_string

def execute(bytecode):
    scope = {}

    ip = 0
    while ip < len(bytecode):
        opcode = bytecode[ip]
        operation = opcode & 0b111
        value = opcode >> 3

        if operation == 0:
            ip += 1

        elif operation == 1:
            print(LIB[value], end=' ')
            ip += 1

        elif operation == 2:  # call
            address = scope.get(value)
            if address:
                execute(address)
            ip += 1

        elif operation == 3:  # is
            scope[value] = bytecode[ip + 1: ip + 3]
            ip += 3

        elif operation == 4:  # to
            scope[value] = scope[bytecode[ip + 1]]
            ip += 2

        elif operation == 5:  # exit
            break

        elif operation == 6:  # emit
            emit_char(value)
            ip += 1

        elif operation == 7:  # ?
            pass

        elif operation == 8:  # array
            pass

        elif operation == 9:  # @
            pass

        elif operation == 10:  # !
            pass

bytecode = [57, 8440, 129, 8704, 129, 8688, 129, 8600, 129, 8704, 129, 8576, 129, 8672,
            129, 8672, 129, 8576, 129, 256, 129, 8728, 129, 8712, 129, 8696, 129, 8616,
            129, 8768, 129, 8680, 129, 8688, 129, 256, 129, 8592, 129, 8792, 129, 8696,
            129, 8688, 129, 8664, 129, 8680, 129, 8616, 129, 8680, 129, 8576, 129, 264,
            129, 5, 0, 3, 2, 5]

print("Disassembled bytecode:")
print(disasm(bytecode))
print("\nExecuting bytecode:")
execute(bytecode)
