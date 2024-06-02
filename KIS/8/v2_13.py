def main(data):
    data = int(data, 10)
    q1 = (data >> 0) & 0b111111
    q2 = (data >> 6) & 0b11
    q3 = (data >> 8) & 0b111111
    q4 = (data >> 14) & 0b111111
    q5 = (data >> 20) & 0b11111
    result = ((q5 << 20) | (q4 << 14) | (q1 << 8) | (q3 << 2) | q2)
    return str(int(result))


print(main('21268962'))
print(main('4777196'))
