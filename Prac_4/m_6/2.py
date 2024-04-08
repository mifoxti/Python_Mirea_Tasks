from typing import List, Dict

OP_NAMES = {0: "push", 1: "op", 2: "call", 3: "is", 4: "to", 5: "exit"}

LIB: Dict[str, callable] = {
    ".": lambda vm: print(vm.stack.pop()),
}

class VM:
    def init(self, code):
        self.stack = []
        self.code = code
        self.pc = 0  # Программный счетчик

    def run(self):
        while self.pc < len(self.code):
            opcode = self.code[self.pc]
            self.pc += 1

            if opcode in OP_NAMES:
                op = OP_NAMES[opcode]
                print(f"\t{op}")
            elif opcode in LIB:
                op = LIB[opcode].name
                print(f"\t{op}")
                LIB[opcode](self)
            else:
                print(f"\t<unknown operation: {opcode}>")

            if opcode == 1:
                # Обработка кода операции
                operand = self.code[self.pc]
                self.pc += 1
                print(f"\t\t{operand}")
                self.stack.append(operand)

# Пример использования
vm = VM([0, 16, 16, 1, 121, 5])
vm.run()
