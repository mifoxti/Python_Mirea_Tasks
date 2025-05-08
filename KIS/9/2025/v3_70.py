import re


def main(text):
    result = {}
    pattern = r'do\s+equ\s*#\(\s*([^\)]*?)\s*\)\s*==>\s*(\w+)\s*;'
    blocks = re.findall(pattern, text)

    for nums_str, key in blocks:
        numbers = [int(n.strip()) for n in re.findall(r'[-]?\d+', nums_str)]
        result[key] = numbers

    return result


input1 = '''| do equ #(#-7491; #-9905 ; #2292 ) ==> diteon_221; end; do equ #(
#5789 ; #-1097 ; #-4781 )==> azalear_622;end; do equ #( #-6453 ; #2150
) ==> aantixe_292; end; |'''

input2 = '''| do equ #( #4323; #-849)==>esri_547; end; do equ #( #4286 ; #-7349 ;
#6910 ; #3606 ) ==> erar;end;|'''

print(main(input1))
print(main(input2))
