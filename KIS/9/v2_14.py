import re


def parse_data_string(data_string):
    data_string = data_string.replace('\n', '').replace(' ', '')
    pattern = r'decl(.*?)isarray\((.*?)\)'
    matches = re.findall(pattern, data_string)
    result = []
    for match in matches:
        var_name = match[0]
        numbers = [int(num.lstrip('#')) if num.startswith('#')
                   else int(num) for num in match[1].split(',')]
        result.append((var_name, numbers))

    return result


# Примеры использования
data_string1 = '<block> | decl tequ_798 is array( #6861 , #3926 ) | |decl beusqu is\narray( #3864 , #-4287 ) | </block>'
data_string2 = "<block>|decl bexe_240 is array( #-5547 , #-560 , #7865 ) || decl usat_128 is array( #-6577 ,#9752 ,#-3056 , #4938 )||decl ingela is array( #-9515,#-5768, #-8365) | |decl rite_396 is array( #-3097 , #-1052 ,#-6545 , #4505 ) |</block>"

print(parse_data_string(data_string1))
print(parse_data_string(data_string2))
