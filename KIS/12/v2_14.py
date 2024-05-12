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
    offset = 4
    a1_offset, offset = parse(buffer, offset, 'uint16')
    a1, _ = parse_b(buffer, a1_offset)
    a2, offset = parse(buffer, offset, 'int16')
    a3, offset = parse(buffer, offset, 'uint64')
    a4, offset = parse(buffer, offset, 'int16')
    a5, offset = parse(buffer, offset, 'int32')
    a6, offset = parse(buffer, offset, 'double')
    a7, offset = parse(buffer, offset, 'int8')
    a8 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        a8.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int16')
    b2 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        b2_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_c(buffer, b2_offset)
        b2.append(val)
    b3, offset = parse(buffer, offset, 'int64')
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'double')
    c2 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'float')
        c2.append(val)
    c3, offset = parse(buffer, offset, 'int64')
    c4 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        c4.append(val)
    c5, offset = parse_d(buffer, offset)
    c6 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        c6.append(val)
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5, 'C6': c6}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int32')
    d2, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'\xffCUH\x00\xa9o\xc5FF\x1c\xfcOm\xef\xffd\xff\xe6\xfc\xefc?\xd8'
            b'\x15\xcb\x9c\xe0\xb5\x04\x10\x00\x08\x00\x00\x00\xbbqh4\xc2$}cX\x96a?'
            b'\xe9Tb\xa2\xe4`\x9a\xbf=\xfb\x14>\xefI\x05\xbf%\x17\x8e\xbd\xb2\xbc\xc7\xa9'
            b'\xcdZ\xa9\x01?#\x88\x00\x00\x00\x05\x00%\xa8\xd8b\x10?O\x07\xcd\x00\x00\x00'
            b'\x05\x00\x00\x00*\xcf\x1fH\x02\x0f\x16\xbf\xef\xf9!\xc0\x86\xbd.\xbf'
            b'\x10\xbc!\xbf\n#\xa4\xbf\x1c\xa2o\xbe.\xb7/}\xafJd\x9e\x1a.\xa0\x00'
            b'\x00\x00\x03\x00e-\xda ~\xbe\xc3\x17\x8b\x00\x00\x00\x03\x00\x00\x00'
            b'h\x00\x00\x00/\x00\x00\x00k\xff\x03\x00\x00\x00\x02\x00\x00\x00\xa1\xdf'
            b"\x9ac\xe7;\x10\xee-X\xe9\x15'(\rB`"))
