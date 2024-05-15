import re


def main(input_string):
    pattern = r"array\s*\(\s*([#\d\s-]+)\s*\)\s*=\s*:\s*(\w+);"
    matches = re.findall(pattern, input_string)
    result = {name: [int(num) if num[0] != '#' else -int(num[1:])
                     for num in re.findall(r'-?\d+', values)]
              for values, name in matches}
    return result


# Примеры использования
input_string1 = "{{ .begin decl array( #5739 #9929 ) =: leer_244;.end. .begin decl array( #-4859#-2904#7744 #-6475 ) =: sodian_737; .end. }}"
input_string2 = "{{ .begin decl array( #-3636 #4187#-749 #9736 )=: arin_93; .end. .begin decl array( #-4802#3825 #-1862 ) =: geer; .end. .begin decl array( #-4519#5667 ) =: rateer; .end. }}"

print(main(input_string1))
print(main(input_string2))
