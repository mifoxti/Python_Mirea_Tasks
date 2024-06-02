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
    a1, offset = parse(buffer, offset, 'int32')
    a2, offset = parse(buffer, offset, 'int16')
    a3_offset, offset = parse(buffer, offset, 'uint32')
    a3, _ = parse_b(buffer, a3_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_c(buffer, adr_offset)
        b1.append(val)
    b2, offset = parse(buffer, offset, 'uint8')
    b3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint32')
        b3.append(val)
    b4 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'double')
        b4.append(val)
    return {'B1': b1, 'B2': b2,
            'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'float')
    c2, offset = parse_d(buffer, offset)
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'double')
    d2 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'int32')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'NBN\xfa\xb9c\xbb#`8\x00\x00\x00V\xbf\x02\xeaz?\xee\xdd\xd1\x96t\x03N;\xd4'
            b'\xc5\xb7\xc7\x8b\x01\xa4t\xb2\x12\r\xe3\xd3^\x9e?9\xe9]\xbf\x06'
            b'\x0f\xae\xbf\xe6\x17oV\xc8\xf2\xe2\xe8?\xf0\x91tp\xe9z\x0ec\t\x8f]mP\xca>='
            b'\xc4\x94EMc\xcf\x9f\x0b\xd5O\x00\x02\x00\x00\x00\x0e\xac\x00\x02\x00'
            b'\x00\x00N\xbf\xe7\xfd[\x0cCv\xf2?\xe3X~,9\xd1\xea\xbf\xda\x92H\x9e'
            b'\x9b]\xc8\xbf\xe0\xe1c\x93Q.^\xbf\xe4\x19^\x0f\xce&\xce?\xdc\n4\xb1'
            b'\x05\x10 '))
