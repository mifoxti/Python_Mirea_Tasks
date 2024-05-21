import re


def main(input_string):
    pattern = r"auto\s*'([^']+)'\s*:\s*@'([^']+)'"
    matches = re.findall(pattern, input_string)
    result = {key: value for key, value in matches}
    return result


# Примеры использования
input_string1 = "<block><: auto 'xeendi' : @'bean'. :>; <: auto 'arries' : @'bean_822'. :>;</block>"
input_string2 = "<block><:auto'bece_285':@'quso_880'. :>;<:auto 'aten_161' : @'erin'.:>;<:auto 'isis':@'lexe'. :>; </block>"

print(main(input_string1))
print(main(input_string2))
