def main(data):
    my_dict = {}
    for name, value in data:
        v = int(value)
        my_dict[name] = v
    W1 = bin(int(my_dict['W1']))[2:].zfill(2)
    W2 = bin(int(my_dict['W2']))[2:].zfill(6)
    W3 = bin(int(my_dict['W3']))[2:].zfill(4)
    W4 = bin(int(my_dict['W4']))[2:].zfill(6)
    return str(int(W4 + W3 + W2 + W1, 2))
