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
    a1, offset = parse(buffer, offset, 'int8')
    a2, offset = parse_b(buffer, offset)
    a3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        a3.append(val)
    a4, offset = parse(buffer, offset, 'int16')
    a5, offset = parse_e(buffer, offset)
    a6, offset = parse(buffer, offset, 'int32')
    a7, offset = parse(buffer, offset, 'float')
    a8, offset = parse(buffer, offset, 'int64')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        val, adr_offset = parse_c(buffer, adr_offset)
        b1.append(val)
    b2, offset = parse(buffer, offset, 'uint64')
    b3 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b3 += (val.decode())
    b4, offset = parse(buffer, offset, 'uint32')
    b5, offset = parse(buffer, offset, 'int32')
    b6 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        b6.append(val)
    b7, offset = parse(buffer, offset, 'int8')
    b8, offset = parse(buffer, offset, 'uint64')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b7, 'B8': b8}, offset


def parse_c(buffer, offset):
    c1, offset = parse_d(buffer, offset)
    c2, offset = parse(buffer, offset, 'double')
    c3, offset = parse(buffer, offset, 'uint32')
    c4, offset = parse(buffer, offset, 'double')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int32')
    d2, offset = parse(buffer, offset, 'uint8')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int32')
    e2, offset = parse(buffer, offset, 'uint64')
    e3, offset = parse(buffer, offset, 'uint64')
    return {'E1': e1, 'E2': e2, 'E3': e3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'kCMBD\x00\x02\x00\x00\x00^pK\x145\x07\xecgH\x00\x02\x00\x00\x00\x90n[\xc5'
            b'\xe8\x1bqX\x9f\x00\x00\x00\x05\x00\x92\xe0\x0c\xb4\x89\x98\xb6\x84s\xa6'
            b'\x00\x00\x00\x02\x00\x00\x00\x97\xc1\x94:[\xb1C!\x1b\x04\x84\xbe\x98'
            b'\xef*\x9e\xeb\xde\xa7XZ\x01\x9eV\xab\xd1\x96\xbe\xce\xe5\xa6A\xc7\x8d{\xa15'
            b'_\xae\xa2\x98\x8c\x87\xb5\xbf\xb3\xeb\xa2D\xbd\xb5 \xab_2!?\xe4\r=\x7f'
            b'd\xd4\xd0\xc9r\xcc\x12\xc7?\xd8\x08\x89H\x0ex\xe4w~\x83\xfc\xbf\xe1\xe0\xf6'
            b'7vj\xbadf\xd5v\x0bM\xd5\x84(\xde\xbd'))
