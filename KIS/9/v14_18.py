import re


def parse_string(input_string):
    pattern = r"define\s+`([\w_]+)\s*<-\s*array\s*\(\s*([^()]+?)\s*\)"
    matches = re.findall(pattern, input_string)
    result = []
    for name, values in matches:
        numbers = [int(num.strip()) for num in values.split(';')]
        result.append((name, numbers))
    return result


# Примеры использования
input_string1 = r"(\begin define `ditice_573<- array(6734; 1260 ;292; -5956 ) \end, \begin define `cera <- array( 4056;-7200 ; -5089 ) \end, \begin define `beis_567 <- array( 4489 ;1402 ;-9852 ) \end,\begin define `eronqu_503 <- array( -3137 ; -2340 ; -7148 ;3680 ) \end, )"
input_string2 = r"( \begin define `cemaqu<- array( 5120 ; 6528) \end,\begin define `rigera<- array(1725 ; 7581 ; 8469 ;-2940 ) \end, \begin define `qurein_404 <- array( -5516; -7715 ) \end, )"

print(parse_string(input_string1))
print(parse_string(input_string2))
