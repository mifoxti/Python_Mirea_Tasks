import re


def main(input_string):
    pattern = re.compile(r'local\s+([a-zA-Z0-9_]+)\s*<==\s*([a-zA-Z0-9_]+);')
    result = {}
    matches = pattern.findall(input_string)

    for match in matches:
        name, value = match
        result[name] = value

    return result


input_string1 = "<sect> [[ local rigexe_112<==leleri_480; ]] [[ local onzaat_596<==teenbi_125; ]] [[local ones_865 <==reza; ]] </sect>"
input_string2 = "<sect> [[ local aorence_516 <==rear_514;]] [[ local esla <==erbe_147; ]] </sect>"

print(main(input_string1))
print(main(input_string2))
