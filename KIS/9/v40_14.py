import re


def main(input_string):
    pattern = r"do\s+loc\s+(\w+)\s*::=\s*(\w+)\.\s*end;"
    matches = re.findall(pattern, input_string)
    return matches


# Примеры использования
input_string1 = "<block> do loc bidi_77::=dizaat. end; do loc raan_702 ::= enso_8. end; do loc tear_621 ::= cetibe. end; </block>"
input_string2 = "<block> do loc orte ::= tein_404. end; do loc enlama_329 ::= orquis. end;do loc anza ::=xeaaan. end; </block>"

print(main(input_string1))
print(main(input_string2))
