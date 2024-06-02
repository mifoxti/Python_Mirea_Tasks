import re


def main(input_string):
    pattern = re.compile(r'\[\[\s*val\s*#(-?\d+)\s*to\s*@"(.*?)"\s*\.\s*\]\]')
    matches = pattern.findall(input_string)
    result = [(name, int(number)) for number, name in matches]
    return result


# Пример использования:
input_string1 = '|| [[val #1091 to @"atesus". ]]; [[ val#7599 to @"quriis". ]]; [[val #-372 to @"sosoed".]]; [[ val#8848 to @"sove_96". ]]; ||'
input_string2 = '|| [[ val#9572 to @"usedin_112".]]; [[val#2823 to @"arat".]]; [[val#-7953 to @"soza". ]];[[ val #6992 to @"arti_240". ]]; ||'

print(main(input_string1))
print(main(input_string2))
