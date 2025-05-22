import re


def main(text):
    pattern = r'\[\s*set\s+(\w+)\s+(\w+)\s*\]'

    matches = re.findall(pattern, text)

    return {key: value for key, value in matches}


s1 = "do [set atxe_487 veis_980 ]; [ set raonbi_971 anes_996 ]; [ set lain_463 enaat]; od"
s2 = "do [ set anteso_118 anis ]; [set teorti gebice_555]; [set biale onenle_417 ]; od"

print(main(s1))
# {'atxe_487': 'veis_980', 'raonbi_971': 'anes_996', 'lain_463': 'enaat'}

print(main(s2))
# {'anteso_118': 'anis', 'teorti': 'gebice_555', 'biale': 'onenle_417'}
