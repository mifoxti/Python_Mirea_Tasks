import re


def main(input_str):
    pattern = r'#\s*(-?\d+)\s*\|\>\s*([\w_]+)\s*;'
    matches = re.findall(pattern, input_str)
    result = [(match[1], int(match[0])) for match in matches]
    return result


# Примеры использования
input_str1 = "<sect>.do declare #-3968|> zaen; .end .do declare #3786|>zaraxe_482;.end </sect>"
input_str2 = "<sect>.do declare#-9802|>userre;.end .do declare #8448\n|>xezati_181;.end .do declare #-7736|> ateti; .end </sect>"

print(main(input_str1))  # Ожидаемый результат: [('zaen', -3968), ('zaraxe_482', 3786)]
print(main(input_str2))  # Ожидаемый результат: [('userre', -9802), ('xezati_181', 8448), ('ateti', -7736)]
