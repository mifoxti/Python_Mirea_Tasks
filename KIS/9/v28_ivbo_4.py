import re


def main(input_string):
    clean_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r'autolist\(([^)]+)\)=:(\w+\.?)'
    matches = re.findall(pattern, clean_string)
    result = []
    for match in matches:
        numbers_str = match[0]
        name = match[1].strip('.')
        numbers = [int(num.replace('#', '')) for num in numbers_str.split(';')]
        result.append((name, numbers))
    return result


# Пример использования
input_string1 = '<sect>|auto list(#4569 ; #-9509 ;#3192 ) =:orarma. |;| auto list( #1286 ; #-9214 ) =: geerle. |; | auto list( #-5670 ; #8232) =: leinso_137. |; | auto list( #-851 ; #-8776; #-9249 ) =: riis.|; </sect>'
input_string2 = '<sect> | auto list(#-313 ; #5253 ) =: adiqu_956.|;| auto list(#288 ; #-577 ; #-8184;#-7187) =:isis. |; </sect>'

parsed_result1 = main(input_string1)
parsed_result2 = main(input_string2)

print(parsed_result1)
print(parsed_result2)
