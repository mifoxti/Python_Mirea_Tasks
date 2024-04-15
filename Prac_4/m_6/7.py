def parse(source):
    tokens = source.split()

    result = []
    stack = []

    for token in tokens:
        if token == '[':
            stack.append([])
        elif token == ']':
            if len(stack) == 1:
                result.append(('push', stack.pop()))
            else:
                top = stack.pop()
                stack[-1].append(top)
        else:
            try:
                value = int(token)
                stack[-1].append(('push', value))
            except ValueError:
                stack[-1].append(('call', token))

    return result


# Пример использования
source = "[ to n  n 2 < [ 1 ] [ n n 1 - fact * ] if ] is fact 5 fact ."
result = parse(source)
print(result)
