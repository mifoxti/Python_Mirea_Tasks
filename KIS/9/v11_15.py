import re


def main(input_string):
    input_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r"let@'(\w+)':=#(-?\d+)"
    matches = re.findall(pattern, input_string)
    result = {name: int(value) for name, value in matches}
    return result


# Пример использования
input_string1 = "do .begin let @'arriso_195' :=#-1964 .end, .begin let @'tea_404' := #-53 .end,.begin let @'quve':= #626 .end,.begin let @'abe_835' := #8486 .end, done"
input_string2 = "do .begin let @'rauser' :=#6846 .end, .begin let @'timaed_198' :=#7349 .end, done"

parsed_result1 = main(input_string1)
parsed_result2 = main(input_string2)

print(parsed_result1)
print(parsed_result2)
