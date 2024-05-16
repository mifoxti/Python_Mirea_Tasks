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
    offset = 4
    a1 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        a1_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_b(buffer, a1_offset)
        a1.append(val)
    a2 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a2 += (val.decode())
    a3_offset, offset = parse(buffer, offset, "uint16")
    a3, _ = parse_c(buffer, a3_offset)
    a4 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'double')
        a4.append(val)
    a5, offset = parse(buffer, offset, "uint32")
    a6, offset = parse(buffer, offset, "uint8")
    a7_offset, offset = parse(buffer, offset, "uint16")
    a7, offset = parse_e(buffer, a7_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint8')
    b2, offset = parse(buffer, offset, 'int16')
    b3, offset = parse(buffer, offset, 'double')
    b4, offset = parse(buffer, offset, 'int16')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint8')
    c2, offset = parse(buffer, offset, 'float')
    c3, offset = parse_d(buffer, offset)
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'uint8')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'float')
    d3, offset = parse(buffer, offset, 'uint8')
    d4, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int64')
    e2, offset = parse(buffer, offset, 'uint8')
    e3 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'int32')
        e3.append(val)
    return {'E1': e1, 'E2': e2, 'E3': e3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'\x04SIH\x03\x00\x00\x00p\x00\x02\x00v\x00\x00\x00x\x00\x16\x80\xc1m\x88\xd5'
            b'\xea?\x96/\x0c+\x9f\xdf\xef?\x88\x96\xe6"\x9a\x18\xe9\xbfRe\xc2\xac\xe8\x86'
            b'\xe9?X\x7ftP\x11\x93\xd7?\xa2\xd4\xd1\x90YL\xe0\xbf\xf6\x95[\x06e\x88'
            b'\x00\x8ab{"m\xb2\xf2\xe5<\xed?f\x11,\x0f>\x0c/\xb4\xf1*k\xde\xbf\xa61)'
            b'\xc6\x01\xfa\xe0\xb3\xf9\xf9R\xe9?\xe0\x18I\x00V\x00c\x00ui\x9a\x1bTt'
            b'?\x9cE\x90Q\x8a\xa6\x03\x1d?\x08x\xc5:\x86\x93\x89}J\xaf\x88U\xeb\xbf'
            b'HX\x8d\xb0\x9ds\xf1\x10!\\\x8c\xfbI&\xadg\xb1\xb8\xbe\xbc\xe0'))
