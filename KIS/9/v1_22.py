import re


def main(input_string):
    input_string = re.sub(r'\s+', '', input_string)
    pattern = re.compile(r'vararray\(#([0-9#-]+)\)=:`([a-zA-Z0-9_]+)')
    result = {}
    matches = pattern.findall(input_string)
    for match in matches:
        numbers_str, name = match
        numbers = [int(num) for num in numbers_str.split('#') if num]
        result[name] = numbers

    return result


# Примеры использования функции
input_string1 = "((| var array( #3062#-8889 #394 #6928) =: `onxeso |,| var array( #3183 #-2862 ) =: `enar|, ))"
input_string2 = "(( | var array( #3636 #-8433 #202) =: `eszaed |,| var array( #-2405 #-6059 #-8558) =: `xere|, |var array( #9149 #5868 #-1164 ) =: `laquen_600|,| var array( #5012 #-9833)=: `bies |,))"

print(main(input_string1))
print(main(input_string2))
