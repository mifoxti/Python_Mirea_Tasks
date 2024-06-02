from struct import *


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
    offset = 5
    a1, offset = parse(buffer, offset, 'int64')
    a2, offset = parse(buffer, offset, 'uint8')
    a3, offset = parse_b(buffer, offset)
    a4, offset = parse(buffer, offset, 'uint64')
    a5, offset = parse(buffer, offset, 'int64')
    a6 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        a6.append(val)
    a7, offset = parse(buffer, offset, 'uint64')
    a8, offset = parse(buffer, offset, 'int32')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1, offset = parse_c(buffer, offset)
    b2 = []
    for _ in range(2):
        a, offset = parse_e(buffer, offset)
        b2.append(a)
    b3, offset = parse_f(buffer, offset)
    b4, offset = parse(buffer, offset, 'uint8')
    b5 = []
    for _ in range(8):
        val, offset = parse(buffer, offset, 'int16')
        b5.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3,
            'B4': b4, 'B5': b5}, offset


def parse_c(buffer, offset):
    c1_offset, offset = parse(buffer, offset, 'uint16')
    c1, _ = parse_d(buffer, c1_offset)
    c2, offset = parse(buffer, offset, 'int8')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'int16')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'uint64')
    d3, offset = parse(buffer, offset, 'int32')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int64')
    e2 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'int8')
        e2.append(val)
    e3, offset = parse(buffer, offset, 'uint64')
    e4, offset = parse(buffer, offset, 'uint8')
    e5, offset = parse(buffer, offset, 'int32')
    e6, offset = parse(buffer, offset, 'uint32')
    return {'E1': e1, 'E2': e2, 'E3': e3,
            'E4': e4, 'E5': e5, 'E6': e6}, offset


def parse_f(buffer, offset):
    f1, offset = parse(buffer, offset, 'int32')
    f2, offset = parse(buffer, offset, 'int64')
    return {'F1': f1, 'F2': f2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'DRCW\x15)\x0f\r\x05\xe3\x97\xf4\xfa0\x86\x00cA\xcd\r\xd6\xfb\xe4\x07'
            b'a?\xc3\xf8\x8b-x\xb6\xfeb\xa6f\xb0Q\xa6 \xeb\x16\xea\xa2\xe1~\xec\xf7'
            b'\xdd\xeca\xb2n\xc4\xc6\xb4\xd3\xb1E\x80\xd5{\x0e;]\x8b\x92s.\xc8\xc9O'
            b'\x90[\xbe\xe5\x9f\xad<4\xc1l\xba\xf8da\x8b\xc83\xf8\xd7\xee\xdb\xed\xd1\xfb'
            b'\x87\xc9S\x1d\xcb\x06X\xa5\xa7@-\xec\xa5\xea\x06_\xac1\x87\x8e'
            b'\x02\x00\x00\x00\x98\x00\xdam\xcdB\x92\xc5<\xb3Q9\x06h\xaa\xf4,\x84f\xd1'
            b'3\xe8;\x91m\x1bt\x9b\xf9r\xf4h\xbbS\xb2G'))
