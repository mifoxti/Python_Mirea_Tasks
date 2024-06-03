import re


def main(input_string):
    cleaned_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r'declarray\(([^)]+)\)=>(\"[^\"]+\")'
    matches = re.findall(pattern, cleaned_string)
    result = {}
    for match in matches:
        numbers_str = match[0]
        name = match[1].strip('"')
        numbers = list(map(int, numbers_str.split(';')))
        result[name] = numbers
    return result


input_string1 = '<%{{decl array(-3461 ; -8340)=> "diisor"}}; {{decl array( -3770 ; 1556 ) => "isgebi_331"}}; {{ decl array( 5436 ;1023)=> "vexebe_255"}}; {{decl array( -3355 ;1559 ) =>"bibege_636"}};%>'
input_string2 = '<% {{decl array(8074 ; -5201 ) => "gelare"}};{{ decl array(1191; 2713)=> "orriis" }}; %>'

parsed_result1 = main(input_string1)
parsed_result2 = main(input_string2)

print(parsed_result1)
print(parsed_result2)
