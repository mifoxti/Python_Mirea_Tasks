def op_add(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a + b)

def op_sub(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a - b)

def op_mul(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a * b)

def op_div(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a // b)

def op_mod(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a % b)

def op_and(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a & b)

def op_or(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a | b)

def op_xor(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a ^ b)

def op_lt(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a < b)

def op_gt(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a > b)

def op_eq(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a == b)

def op_shift_left(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a << b)

def op_shift_right(stack, scope):
    b = stack.pop()
    a = stack.pop()
    stack.append(a >> b)

def op_if(stack, scope):
    false_block = stack.pop()
    true_block = stack.pop()
    condition = stack.pop()
    if condition:
        execute(true_block, debug=False)
    else:
        execute(false_block, debug=False)

def op_for(stack, scope):
    body = stack.pop()
    count = stack.pop()
    for _ in range(count):
        execute(body, debug=False)

def op_emit(stack, scope):
    value = stack.pop()
    print(chr(value), end='')

def op_array(stack, scope):
    size = stack.pop()
    stack.append([0] * size)

def op_at(stack, scope):
    index = stack.pop()
    array = stack.pop()
    stack.append(array[index])

def op_store(stack, scope):
    value = stack.pop()
    index = stack.pop()
    array = stack.pop()
    array[index] = value

def op_drop(stack, scope):
    stack.pop()

def op_dup(stack, scope):
    value = stack[-1]
    stack.append(value)

def op_cr(stack, scope):
    print()

# Заполнение scope библиотекой операций
scope = {}
for idx, op_name in enumerate(LIB[1:], start=1):
    scope[op_name] = globals()[f"op_{op_name}"]

# Пример использования
source = """
[ to a  a a ] is dup
[ to a ] is drop
[ 10 emit ] is cr
[
  to gen to scale to bits
  1 gen [ drop scale * ] for to width 
  width dup * array to buf
  width dup * [ to i  35 buf i ! ] for
  width scale /
  gen [ drop
    dup to block
    width [ to y
      width [ to x
        x block / scale % to loc-x
        y block / scale % to loc-y
        loc-y scale * loc-x + to loc-pos
        bits loc-pos >> 1 & [ ] [
          32 buf y width * x + !
        ] if
      ] for
    ] for
    scale /
  ] for drop
  width [ to y
    width [ to x  buf y width * x + @ emit ] for cr 
  ] for
] is fractal ? 3 3 fractal
"""

bytecode = parse(source)
execute(bytecode)
