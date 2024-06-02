import re


def main(input_string):
    cleaned_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r'auto(\w+)<==\{([-\d.]+)\}'
    matches = re.findall(pattern, cleaned_string)

    result = {}
    for match in matches:
        variable_name = match[0]
        numbers_str = match[1]
        numbers = list(map(int, numbers_str.split('.')))
        result[variable_name] = numbers

    return result


# Пример использования
input_string1 = "<<auto quer_740 <== { -7291 . 4101 . -5923 } auto anesso_391 <=={-8441 . 2350 . -4502 . -5086 } auto biat <== { -6363 . -4483 . -1468 . 8157 }auto rain <=={ 3592 . 2627 . 7097 . 3246 }>>"
input_string2 = "<<auto aleve_569 <=={ 2135 . 6670 }auto azaes_318 <=={ -4883 . 9473 . 3280 . -2552 } auto mabice_255 <== { 7025 . -1704 . 6916 . 9292}auto edtied_586 <=={-8643 . -8061 . -5392 } >>"

parsed_result1 = main(input_string1)
parsed_result2 = main(input_string2)

print(parsed_result1)
print(parsed_result2)
