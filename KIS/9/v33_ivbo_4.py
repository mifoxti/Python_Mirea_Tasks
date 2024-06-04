import re


def main(input_string):
    input_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r'defq\((\w+)\)<=array\(([^)]+)\)'
    matches = re.findall(pattern, input_string)
    result = {}
    for name, values in matches:
        values_list = [value.strip() for value in values.split(';')]
        result[name] = values_list
    return result


# Пример использования
input_string1 = "do ((def q(veen_47)<=array( requon ; rale_488 ; laza_330 ).)), (( def q(biceus)<= array( inbige; tebedi_726 ).)), od"
input_string2 = "do((def q(bian_276)<= array( laedve ; eris ). )), (( def q(usisen) <= array(qugea_93; laria_667 ;inxequ ). )), od"

parsed_result1 = main(input_string1)
parsed_result2 = main(input_string2)

print(parsed_result1)
print(parsed_result2)
