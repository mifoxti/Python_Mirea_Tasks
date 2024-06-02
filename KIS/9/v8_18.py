import re


def main(input_str):
    pattern = r'define\s+([\w_]+)\s*\|\>\s*`([\w_]+);'
    matches = re.findall(pattern, input_str)
    result = [(match[1], match[0]) for match in matches]
    return result


# Примеры использования
input_str1 = "begin <data> define vein|>`tedi_857; </data>, <data>define edle|>`biesge_877; </data>,end"
input_str2 = "begin <data> define lege_236 |> `edce_594;</data>, <data> define geza |> `erat; </data>, <data> define istexe_543|> `rarion;</data>, end"

print(main(input_str1))  # Ожидаемый результат: [('tedi_857', 'vein'), ('biesge_877', 'edle')]
print(main(
    input_str2))  # Ожидаемый результат: [('edce_594', 'lege_236'), ('erat', 'geza'), ('rarion', 'istexe_543')]
