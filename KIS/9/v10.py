import re


def main(input_string):
    cleaned_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r'defq\(([\w_]+)\)<\|list\(([^)]+)\)\.:>'
    matches = re.findall(pattern, cleaned_string)
    result = {}
    for match in matches:
        key = match[0]
        values = match[1].split(',')
        result[key] = [value.strip() for value in values]
    return result


# Пример использования
input_string1 = """do<: def q(ana) <|list( esveon , lacere_17 , leti , onaten_286).:>.
<: def q(maveer)<| list( maza , bire_150). :>. <: def q(bere_746)
<|list(este, reed_980 ).:>. od"""

input_string2 = """do <: def q(eddi) <| list( quleve, rara_153 , orma_224). :>. <: def
q(rasoin_839) <| list(enused_506 ,arsoti ). :>. <: def q(dierer_167)<|
list( orace_499 ,anausqu ). :>.<: def q(rain)<| list(bia , labiti_862
).:>. od"""

parsed_result1 = main(input_string1)
parsed_result2 = main(input_string2)

print(parsed_result1)
print(parsed_result2)
