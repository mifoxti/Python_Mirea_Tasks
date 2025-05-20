import re


def main(input_string):
    pattern = r"data\s+list\s*\(\s*([#;\s\d-]+)\s*\)\s*->\s*@'([\w_]+)'"
    matches = re.findall(pattern, input_string)

    result = {}
    for nums_str, name in matches:
        numbers = re.findall(r'#(-?\d+)', nums_str)
        int_list = [int(num) for num in numbers]
        result[name] = int_list

    return result


s1 = """(( ((data list( #9319 ;#-3704 )-> @'erxe_350'. )). (( data list( #2443
; #6594;#-7714 ; #-1690 ) -> @'esares_935'.)). ((data list( #6438;
#-7037; #5953 ; #5230 ) -> @'maordi'. )). ((data list(#7899 ; #-2615 )
-> @'isza'. )).))"""

s2 = """(((( data list( #-1600 ; #-6343 ) ->@'maat'. )). ((data list( #2026 ;
#-4248;#-3089; #9541 ) -> @'sovela'. )). (( data list( #-1403 ; #1439
; #-9618 )-> @'esceat_957'.)). ))"""

print(main(s1))
# {'erxe_350': [9319, -3704], 'esares_935': [2443, 6594, -7714, -1690],
#  'maordi': [6438, -7037, 5953, 5230], 'isza': [7899, -2615]}

print(main(s2))
# {'maat': [-1600, -6343], 'sovela': [2026, -4248, -3089, 9541],
#  'esceat_957': [-1403, 1439, -9618]}
