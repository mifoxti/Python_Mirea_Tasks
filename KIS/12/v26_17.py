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
    a1, offset = parse(buffer, offset, 'int16')
    a2 = []
    for _ in range(4):
        b3_offset, offset = parse(buffer, offset, 'uint16')
        val, _ = parse_b(buffer, b3_offset)
        a2.append(val)
    a3, offset = parse(buffer, offset, 'uint64')
    a4_offset, offset = parse(buffer, offset, 'uint16')
    a4, _ = parse_c(buffer, a4_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'float')
    b2, offset = parse(buffer, offset, 'float')
    b3, offset = parse(buffer, offset, 'float')
    b4 = ''
    for _ in range(6):
        val, offset = parse(buffer, offset, 'char')
        b4 += (val.decode())
    b5, offset = parse(buffer, offset, 'int64')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int64')
    c2, offset = parse(buffer, offset, 'float')
    c3, offset = parse_d(buffer, offset)
    c4, offset = parse_e(buffer, offset)
    c5, offset = parse(buffer, offset, 'float')
    return {'C1': c1, 'C2': c2,
            'C3': c3, 'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint8')
    d2, offset = parse(buffer, offset, 'int16')
    d3, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int32')
    e2, offset = parse(buffer, offset, 'uint8')
    e3 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'uint8')
        e3.append(val)
    e4 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        e4.append(val)
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4}, offset


def main(data):
    result, _ = parse_a(data, 4)
    return result


from pprint import pprint

pprint(main(b'#QVO\x86\xb0\x18\x002\x00L\x00f\x00\xef\x85f~\xf5T\xa1\x98\x82\x00'
            b'\xc0\xb9\xd7\xbe\x85\xfe\x96>\x9c\xc2\xfe\xbegykrhb\xca\xe8\xf9_\x1d\xb2'
            b'n\x16b\xb9\x12\xbe\xd2\xc4\\?c\xd7k\xbfjtsgsf\xbd\xc0\x90\x91'
            b'\x84\xc3\xef\xfe~a#\xbf\xc5\x92e?\x82\x83\xdc>gbeaatR\xc9\x0f?mo\x1fM\x9cp'
            b'\xe0\xbe\xdf\x99\xc3\xbe\xf2\x9cF?ozvytx\x1c\x84\x19\xabOK?\xdd;\x87g\x0f'
            b'\xb6\x0c\xc5W\xcffeT\x05?\xfc\xf6\xd2t\x0f!\xa2\x80\xaet;\xc2\xc9\x02'
            b'\x00\x80\x00\x00\x00\xd6,\x10>'))
