OP_NAMES = {0 : 'push', 1 : 'op', 2 : 'call', 3 : 'is', 4 : 'to', 5 : 'exit'}

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


def emit_char(code) :
    print(chr(code), end='')


def disasm(bytecode) :
    result_string = []

    ip = 0
    while ip < len(bytecode) :
        opcode = bytecode[ip]
        operation = opcode & 0b111
        value = opcode >> 3

        if operation == 0 and value == 0 :
            pass

        elif operation == 0 :
            result_string.append(value)

        elif operation == 1 :
            result_string.append(LIB[value])

        elif operation == 2 :  # call
            result_string.append(OP_NAMES[operation])

        elif operation == 3 :  # is
            result_string.append(OP_NAMES[operation])

        elif operation == 4 :  # to
            result_string.append(OP_NAMES[operation])

        elif operation == 5 :  # exit
            break

        elif operation == 6 :  # emit
            result_string.append(OP_NAMES[operation])

        elif operation == 7 :  # ?
            result_string.append(OP_NAMES[operation])

        elif operation == 8 :  # array
            pass

        elif operation == 9 :  # @
            pass

        elif operation == 10 :  # !
            pass

        ip += 1

    return result_string


def execute(bytecode) :
    stack = []
    scope = {}

    ip = 0
    while ip < len(bytecode) :
        opcode = bytecode[ip]
        operation = opcode & 0b111
        value = opcode >> 3

        if operation == 0 :  # push
            stack.append(value)

        elif operation == 1 :  # op
            print(LIB[value], end=' ')

        elif operation == 2 :  # call
            address = scope.get(value)
            if address :
                execute(address)

        elif operation == 3 :  # is
            scope[value] = bytecode[ip + 1 : ip + 3]
            ip += 2

        elif operation == 4 :  # to
            scope[value] = scope[bytecode[ip + 1]]
            ip += 1

        elif operation == 5 :  # exit
            break

        elif operation == 6 :  # emit
            emit_char(value)

        elif operation == 7 :  # ?
            condition = stack.pop()
            true_address = bytecode[ip + 1]
            false_address = bytecode[ip + 2]
            ip += 2
            ip = true_address if condition else false_address

        ip += 1


bytecode = [
    17, 8, 5, 2, 2, 8, 9, 10, 17, 5, 4, 2, 16, 65, 0, 16, 105, 5, 72, 11, 40, 10,
    121, 5
]

print("Disassembled bytecode:")
print(disasm(bytecode))
print("\nExecuting bytecode:")
execute(bytecode)
