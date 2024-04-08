OP_NAMES = {0: 'push', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}

LIB = {
    '+': 'not_implemented',
    '-': 'not_implemented',
    ' * ': 'not_implemented',
    '/': 'not_implemented',
    '%': 'not_implemented',
    '&': 'not_implemented',
    '|': 'not_implemented',
    '^': 'not_implemented',
    '<': 'not_implemented',
    '>': 'not_implemented',
    '=': 'not_implemented',
    '<<': 'not_implemented',
    '>>': 'not_implemented',
    'if': 'not_implemented',
    'for': 'not_implemented',
    '.': 'not_implemented',
    'emit': 'not_implemented',
    '?': 'not_implemented',
    'array': 'not_implemented',
    '@': 'not_implemented',
    '!': 'not_implemented',
    'add': 'not_implemented'
}



def disasm(bytecode):
    lines = []
    pc = 0

    while pc < len(bytecode):
        op_code = bytecode[pc] & 0b111
        argument = bytecode[pc] >> 3

        if op_code == 0:  # push
            lines.append(f'{OP_NAMES[op_code]} {argument}')
        elif op_code == 1:  # op
            lines.append(f"{OP_NAMES[op_code]} '{LIB.get(argument, '+')}'")
        elif op_code == 2:  # call
            lines.append(f'{OP_NAMES[op_code]} {argument}')
        elif op_code == 3:  # is
            lines.append(f'{OP_NAMES[op_code]} {argument}')
        elif op_code == 4:  # to
            lines.append(f'{OP_NAMES[op_code]} {argument}')
        elif op_code == 5:  # exit
            lines.append(f'{OP_NAMES[op_code]} {argument}')
        elif op_code ==15:
            lines.append(f"{OP_NAMES[op_code]} '{LIB.get(argument, '.')}'")

        pc += 1

    return lines

# Пример использования
result = disasm([0, 16, 16, 1, 121, 5])
for line in result:
    print(line)