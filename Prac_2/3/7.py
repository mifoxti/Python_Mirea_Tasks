print((lambda num: num % sum(map(int, str(num))) == 0)(int(input("Введите число: "))))

