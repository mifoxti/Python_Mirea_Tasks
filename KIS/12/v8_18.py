from struct import *


def parse(buffer, offset, type, order='>'):
    pattern = {
        'float': 'f',
        'double': 'd',
        'char': 'c',
        'int8': 'b',
        'uint8': 'B',
        'int16': 'h',
        'uint16': 'H',
        'int32': 'i',
        'uint32': 'I',
        'int64': 'q',
        'uint64': 'Q'
    }[type]
    size = calcsize(order + pattern)
    value = unpack_from(order + pattern, buffer, offset)[0]
    return value, offset + size


def parse_a(buffer, offset):
    offset = 4
    a1, offset = parse(buffer, offset, 'uint8')
    a2, offset = parse_b(buffer, offset)
    a3, offset = parse(buffer, offset, 'int64')
    a4 = ''
    for _ in range(4):
        val, offset = parse(buffer, offset, 'char')
        a4 += (val.decode())
    a5 = ''
    for _ in range(6):
        val, offset = parse(buffer, offset, 'char')
        a5 += (val.decode())
    a6, offset = parse(buffer, offset, 'int16')
    a7 = []
    for _ in range(3):
        a7_offset, offset = parse(buffer, offset, 'uint32')
        val, _ = parse_d(buffer, a7_offset)
        a7.append(val)
    a8, offset = parse(buffer, offset, 'uint32')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'double')
    b2, offset = parse(buffer, offset, 'int16')
    b3, offset = parse(buffer, offset, 'uint32')
    b4, offset = parse_c(buffer, offset)
    b5, offset = parse(buffer, offset, 'uint64')
    b6, offset = parse(buffer, offset, 'uint32')
    return {'B1': b1, 'B2': b2,
            'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int8')
    c2, offset = parse(buffer, offset, 'uint64')
    c3, offset = parse(buffer, offset, 'int64')
    c4, offset = parse(buffer, offset, 'uint64')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint8')
    d2, offset = parse(buffer, offset, 'int8')
    d3, offset = parse(buffer, offset, 'uint16')
    d4 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'int16')
        d4.append(val)
    d5, offset = parse(buffer, offset, 'uint8')
    d6, offset = parse(buffer, offset, 'uint16')
    d7, offset = parse(buffer, offset, 'uint64')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'LLSJ\x9c?\xc9\xc3U\x85<\x02 \xc4\xb1\xafs\x02m\xfba\xd9*J\xff\xc7\xd5\xc4'
            b'\xbeK7\xc8a\x10\xcb\xfd\xf7\x9d7\xf0\x86\xbd\xb2?[\x94\xe1\x11\xe1$\x98\x13'
            b'x\x94\rV\x9c\xa9!\xf9|\x8c\xcc<vevtmvalpz{\x88\x00\x00\x00\\\x00\x00\x00w'
            b'\x00\x00\x00\x92f\xd6^\x86\x92\xc7\x8b\x95$1\r\x8a #\x19\x94\x9a\x84\xc0\xf6'
            b"I-<\xe2\xd7\xe3uK'q\xc2T\xd2}3\xa2\x81f\xf9U@\x99\x1b\xddT\x9d\xe8k"
            b'\xee\x8b$\x97\ns\xe4$\x88\x9f<h\x19j\xf3\x12\x8eu\xd1\x00\x04\xb9w\x90'
            b'\xdc\xe5\x1e\xed\x8e\xe4\xb1{%\xab\xb4\xb5\x94'))
