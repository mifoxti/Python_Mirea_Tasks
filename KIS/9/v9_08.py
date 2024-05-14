import re


def main(input_string):
    input_string = input_string.replace(" ", "").replace("\n", "")
    pattern = r'\[\[(.*?)\]\]'
    blocks = re.findall(pattern, input_string)
    result = []
    for block in blocks:
        key_values = block.split("to")
        key = key_values[1]
        values = re.findall(r'@"(.*?)"', key_values[0])
        result.append((key, values))

    return result


# Пример использования
input_string = r'\begin [[opt [ @"qugege_188" ; @"rege_813" ;@"enenza" ] to ustien_537]][[opt [ @"tiin_166" ;@"ononqu_87" ; @"mate_571" ] to isriti_401]] \end'
parsed_result = main(input_string)
print(parsed_result)
input_string = r'\begin [[opt[@"angera_788" ; @"issoce" ]to xera_425 ]] [[ opt [ @"usesor_215" ; @"maza_457" ; @"isesge_962" ; @"rima" ] to georer_871]] \end'
parsed_result = main(input_string)
print(parsed_result)