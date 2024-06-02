import re


def main(input_string):
    cleaned_string = re.sub(r'\s+', '', input_string)
    pattern = re.compile(r'beginoption(\w+)is#\((.*?)\)end')
    matches = pattern.findall(cleaned_string)
    result = []
    for match in matches:
        name, values_str = match
        values = re.findall(r'#-?\d+', values_str)
        values = [int(value.replace('#', '')) for value in values]
        result.append((name, values))
    return result


# Пример использования
input_string1 = '| begin option erleat is #( #1898 ,#-1953, #3926)end begin option eranra is #(#660,#-3177)end begin option isisus_882 is#(#-3667,#-6968, #-2529 )end begin option zaante_196 is #(#5250, #-574,#2019 , #-4497 ) end |'
input_string2 = '| begin option lale_525 is #( #8520, #2427 ,#-5338 , #9348)end begin option receaed_815 is#(#-8297 , #2046, #-8212 , #-9447 ) end |'

print(main(input_string1))
print(main(input_string2))
