from pprint import pprint
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
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        a1_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_b(buffer, a1_offset)
        a1.append(val)
    a2, offset = parse(buffer, offset, 'uint32')
    a3, offset = parse(buffer, offset, 'uint32')
    a4, offset = parse_d(buffer, offset)

    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1 = ''
    for _ in range(2):
        val, offset = parse(buffer, offset, 'char')
        b1 += (val.decode())
    b2, offset = parse(buffer, offset, 'int16')
    b3_offset, offset = parse(buffer, offset, 'uint32')
    b3, _ = parse_c(buffer, b3_offset)
    b4, offset = parse(buffer, offset, 'int32')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint32')
    c2, offset = parse(buffer, offset, 'int8')
    c3, offset = parse(buffer, offset, 'uint8')
    c4 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'int16')
        c4.append(val)
    c5, offset = parse(buffer, offset, 'int8')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int16')
    d2, offset = parse(buffer, offset, 'uint64')
    d3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        d3.append(val)
    d4, offset = parse(buffer, offset, 'int64')
    d5 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        d5.append(val)
    d6, offset = parse(buffer, offset, 'int64')
    d7, offset = parse(buffer, offset, 'uint8')
    d8, offset = parse(buffer, offset, 'double')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7, 'D8': d8}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'\xcePPH\x02\x00\x00\x00}\x00\x00\x00\x0b\x8b\x11\xb0G\xfd\xe4\xfa'
            b'H\xa8\x85\xf3\x1a\xd2k?\xd8o\x02\x00\x00\x00\x81\x00\x00\x00\xed\xd7JFR9'
            b'\xba\x15\x04\x00\x00\x00\x83\x00\x00\x00\xa531\x96\x93\xcfa\xa0Z\x80'
            b'\xc2 \x96lU\xd6?\x03\x05\xb65k\xe1\x1f\xab\t[7\x10\xfa_\x05dv\x9d\xe4G\x00'
            b"\x00\x00\xe9\x05\x08W\xf5\x16\xd691'\xad\xcd)\xf7\xc2\xf9nUujq4\xfcb\x00\x00"
            b'\x00$\x9b\xd0ZV\x00q\x00-\x9c\xa18\xdc\xbd\xa2\xd2M\xbf=\x0c\xac;J'
            b'\r\xa0\xbe'))
