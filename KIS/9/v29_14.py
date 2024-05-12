import re


def main(input_string):
    result = {}
    string = input_string.replace('\n', '')
    string = string.replace(' ', '')
    pattern = (r"var\s*(\w+)\s*<\|\s*array\("
               r"\s*((?:-?\d+\s*\.\s*)*-?\d+(?:\s*\.\s*-?\d+)*)\s*\);")
    matches = re.findall(pattern, input_string)
    for match in matches:
        key = match[0]
        values = [int(num.strip()) for num in match[1].split('.')]
        result[key] = values
    return result

from pprint import pprint
# Пример использования
input_string = "[[ [[var beis <|array( 5520 . -9316 . 6727 . 6829 ); ]] [[var tegeso <| array( -9538 . -4873 . 6723 . 8606 );]] [[var maus_676 <| array( 3622 . -9777 . 9609 . 5274 ); ]] [[ var abearra_802 <| array( 6956 . 9393); ]] ]]"
print(main(input_string))
