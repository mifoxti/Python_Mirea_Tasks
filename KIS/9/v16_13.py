import re


def main(input_string):
    pattern = r"declare\s+(\w+)\s*<-\s*([-+]?\d+);"
    matches = re.findall(pattern, input_string)
    result = {variable: int(value) for variable, value in matches}
    return result


# Примеры использования
input_string1 = "| || declare temaqu <- -4396; ||.||declare biraes<- -7021; ||. ||declare inan_816 <- 5413; ||.|| declare rive<- -1588; ||. |"
input_string2 = "| || declare enri<- -1951; ||.||declare ditiri <- 2752; ||.||declare xequ <- -6930; ||. || declare atbear <- 4212; ||. |"

print(main(input_string1))
print(main(input_string2))
