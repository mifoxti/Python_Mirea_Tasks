import re


def main(input_string):
    pattern = r"global\s+@'([^']+)'\s*<-\s*@'([^']+)'"
    matches = re.findall(pattern, input_string)
    return matches


# Примеры использования
input_string1 = "<section> { global @'ededat'<- @'xequxe_618'.}, { global @'ator_12' <- @'arbe_231'. },</section>"
input_string2 = "<section> {global @'rier' <- @'enin_804'. }, { global @'inquri' <- @'dianat'.}, { global @'rabees' <- @'quteza'.},</section>"

print(main(input_string1))
print(main(input_string2))
