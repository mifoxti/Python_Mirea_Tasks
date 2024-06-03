import re


def parse_string(input_string):
    cleaned_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r'<section>new(\w+)=>(\w+).</section>'
    matches = re.findall(pattern, cleaned_string)
    result = [(match[1], match[0]) for match in matches]
    return result


# Пример использования
input_string1 = 'do<section>new larera => lamare. </section>,<section> new onata => beusar. </section>, <section> new tecera_226 =>anarqu_742. </section>, end'
input_string2 = 'do<section>new usan =>inon. </section>, <section> new atve_79=> atar_286.</section>, end'

parsed_result1 = parse_string(input_string1)
parsed_result2 = parse_string(input_string2)

print(parsed_result1)
print(parsed_result2)
