import re


def parse_string(input_string):
    cleaned_string = input_string.replace(' ', '').replace('\n', '')
    pattern = r'set(\w+)=:q\((\w+)\);'
    matches = re.findall(pattern, cleaned_string)
    result = [(value, key) for key, value in matches]
    return result


# Пример использования
input_string = "<%<% set sora_652 =: q(didi); %><% set isbila=: q(arxe_571); %> %>"
output = parse_string(input_string)
print(output)
input_string = "<% <% set eder_361 =: q(zaedor);%> <% set lace_792 =: q(onat_597);%><% set rate_475 =: q(rian_132); %> <% set qubi_79 =: q(eden_842); %> %>"

output = parse_string(input_string)
print(output)
