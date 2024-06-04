import re


def main(input_string):
    input_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r'domake"(\w+)"::=#(-?\d+);'
    matches = re.findall(pattern, input_string)
    result = [(name, int(value)) for name, value in matches]
    return result


# Пример использования
input_string1 = '.begin do make "ceage" ::= #8579; end; do make "orar_258" ::= #6317; end; do make "arin" ::= #8260; end; do make "reis" ::= #9356; end;.end'
input_string2 = '.begin do make "ateve" ::= #-4727; end; do make "quinxe_819" ::= #-630; end; do make "ana" ::= #-2448; end; do make "enin_114" ::= #-2419; end;.end'

parsed_result1 = main(input_string1)
parsed_result2 = main(input_string2)

print(parsed_result1)
print(parsed_result2)
