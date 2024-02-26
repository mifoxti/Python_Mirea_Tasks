def power_gen(power):
    print("def power(x):")
    print("    result = 1")
    while power > 0:
        if power & 1 == 1:
            print("    result = result * x")
        power >>= 1
        if power > 0:
            print("    x = x * x")
    print("    return result")


power_gen(5)