from struct import *


# РАБОТАЕТ
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
    offset = 5
    a1 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a1 += (val.decode())
    a2, offset = parse(buffer, offset, 'int32')
    a3, offset = parse(buffer, offset, 'int32')
    a4, offset = parse(buffer, offset, 'double')
    a5, offset = parse(buffer, offset, 'int16')
    a6, offset = parse_b(buffer, offset)
    a7, offset = parse(buffer, offset, 'uint64')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        b1_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_c(buffer, b1_offset)
        b1.append(val)
    b2, offset = parse(buffer, offset, 'uint16')
    b3, offset = parse_d(buffer, offset)
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int16')
    c2 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'uint32')
        c2.append(val)
    c3, offset = parse(buffer, offset, 'uint32')
    c4, offset = parse(buffer, offset, 'int64')
    c5, offset = parse(buffer, offset, 'uint8')
    c6, offset = parse(buffer, offset, 'uint16')
    return {'C1': c1, 'C2': c2,
            'C3': c3, 'C4': c4,
            'C5': c5, 'C6': c6}, offset


def parse_d(buffer, offset):
    d1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint64')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'uint8')
    return {'D1': d1, 'D2': d2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'9JDTK\x00\x00\x00\x02\x00\x00\x008\x87?~#\xa8\xccG\xe0?\xe6\xc7M)\xa4Q'
            b'\x8a\xde\xfa\x00\x00\x00\x02\x00\x00\x00t\x04\xa7\x00\x02\x00\x00\x00x\xb4'
            b't:^qqQ\xe9\xdcvn\x10\xb7\xcf&\x99\xb7zk~\xb0\x0e\x92\x06X<\x1e\xa0\xaa'
            b'\x8fd\xe8\xb7\xf3\xe2E\xbeH\xa9/\x1bw\xfaM\xb1\x0f\xf5\x18\xc6\xfaj\x13D'
            b'\xcaW\x1e\xc4H\x8c\x8fv]\xbc\xeaG\xcd\x95y\\\x00:\x00W\xac\x84\xe5\x0f'
            b'z\xf5r\x9f\x0c[\x02\xe1\r-!2'))
