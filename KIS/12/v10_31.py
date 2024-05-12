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
    offset = 3
    a1, offset = parse(buffer, offset, 'uint16')
    a2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        a2.append(val)
    a3 = []
    for _ in range(2):
        e, offset = parse_b(buffer, offset)
        a3.append(e)
    a4, offset = parse(buffer, offset, 'int8')
    a5 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        a5_char, adr_offset = parse(buffer, adr_offset, 'char')
        a5 += a5_char.decode()
    a6, offset = parse_d(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint64')
    b2, offset = parse_c(buffer, offset)
    b3, offset = parse(buffer, offset, 'double')
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint8')
    c2, offset = parse(buffer, offset, 'uint8')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int32')
        d2.append(val)
    return {'D1': d1, 'D2': d2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'EQM\xf8\xee\x03\x00>\x00\x00\x00\xe9t\xe2N\x11\x819\xf5:\x15\xa8\x01\xdb'
            b"\xa1h\xb6\xdc?\xa8U\xfcL\x97'X\xeagY\x10r\xa4\x89\x1e\x86\xba?j\x02\x00D\x00"
            b'\x00\x00\xc6Ns>\x02\x00F\x00\xdb\xdd%\x04\xf7%gukaY\xea\x83oK\x8a'))
