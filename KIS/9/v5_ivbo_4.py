import re


def main(input_string):
    cleaned_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r"var@'([\w_]+)'#(-?\d+)"
    matches = re.findall(pattern, cleaned_string)
    result = {match[0]: int(match[1]) for match in matches}
    return result


# Пример использования
input_string1 = "| var @'anisen' #-9828 |,| var @'titius_841' #2624 |,| var @'rexeon'#3319 |,"
input_string2 = "|var @'tezabe_469'#2214 |, | var @'enenge_116' #7310|,"

parsed_result1 = main(input_string1)
parsed_result2 = main(input_string2)

print(parsed_result1)
print(parsed_result2)
