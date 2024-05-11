from struct import *


# РАБОТАЕТ
def parse(buffer, offset, type, order='<'):
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
    offset = 3
    a1, offset = parse(buffer, offset, 'float')
    a2, offset = parse_b(buffer, offset)
    a3, offset = parse(buffer, offset, 'int32')
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b1 += (val.decode())
    b2 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        b2_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_c(buffer, b2_offset)
        b2.append(val)
    b3, offset = parse_d(buffer, offset)
    b4, offset = parse(buffer, offset, 'int64')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        c1.append(val)

    c2, offset = parse(buffer, offset, 'uint8')
    c3, offset = parse(buffer, offset, 'uint64')
    c4, offset = parse(buffer, offset, 'int32')
    c5 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'uint8')
        c5.append(val)
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'float')
    d3, offset = parse(buffer, offset, 'int64')
    d4, offset = parse(buffer, offset, 'uint32')
    d5, offset = parse(buffer, offset, 'int8')
    d6, offset = parse(buffer, offset, 'uint8')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4, 'D5': d5, 'D6': d6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'NED\xd5\x81x?\x07\x00\x00\x009\x00\x02\x00\x00\x00t\x00\x00\x00\x02\x00|'
            b'\x00\x00\x00\x99\xcaa?ZAQ\x12\xc3\x06\x97\x1c\xd3\x96\xe5Q\xdcAq\x96\xd4'
            b'\x8fuO\x10\xecyG\xb0\x17rduxchz\x89\xba3\x7f\x02\x00\x00\x00@\x00*\xf4'
            b'\xc4\x0c\x17\xe3ZV\x8c\xa5\x95I\xa8z\xc5\xc5\xe8\xbe\xbf\xe2\xb2\x03'
            b'\x00\x00\x00Y\x00\x8a5gM\x884)\xf70-^0\x9d\xf5\x01D\x00\x00\x00_\x00\x00\x00'
            b'W7'))
