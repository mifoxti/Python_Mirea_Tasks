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
    a1, offset = parse(buffer, offset, 'uint64')
    a2 = ''
    for _ in range(2):
        val, offset = parse(buffer, offset, 'char')
        a2 += (val.decode())
    a3, offset = parse(buffer, offset, 'int8')
    a4 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        a1_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_b(buffer, a1_offset)
        a4.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        b1.append(val)
    b2, offset = parse_c(buffer, offset)
    b3, offset = parse(buffer, offset, 'uint8')
    b4, offset = parse(buffer, offset, 'int32')
    b5, offset = parse_d(buffer, offset)
    b6, offset = parse(buffer, offset, 'int32')
    b7 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'uint64')
        b7.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b7}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint8')
    c2, offset = parse(buffer, offset, 'double')
    c3, offset = parse(buffer, offset, 'float')
    c4, offset = parse(buffer, offset, 'int8')
    c5, offset = parse(buffer, offset, 'uint8')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'LZNW\x89{\xeb\xe89b\xadftk\x9d\x02\x00\x00\x00\xb2\x00\x00\x00:\xe204U'
            b'\xebd\xb1\x02\x00\x00\x00\x17\x00\xdd\x0c\x02r\xc0\x021\xd0?\xfe\x86'
            b'\xe4\xbe\x11M5\xee\xcc\xfb\x94j\xe9v?\x06\x00\x00\x00\x19\x00\x00\x00\xf2_z'
            b'?\xe6\xb8e\to\x0b9\xe1\xd8K\xe2\x1a\xad\xadhwS\x80\xa1E?`\xfa|R\xd0\xb0'
            b'\xe2\xa1\xe5Ng\x9a\xc5\x90\x03\x00\x00\x00e\x00\xa5\x92\x0bS9\x01\xe3\xe6?('
            b'\xf7\x17\xbf\xdad&`\x87\x0e\xfe}_e\xbf\x04\x00\x00\x00h\x00\x00\x00L\xee8?a!'
            b'\xb4\xab\xc3\xf0\x7f\x89\xd26\xbe\x05\xf0\x1d\xac\x02\x81\x9b\xab\xe3!\xcf'
            b'\xf6*\x19\\\x1d\x87\x1f\x00\x00\x00l\x00\x00\x00'))
