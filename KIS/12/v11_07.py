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
    a1 = []
    for _ in range(4):
        b3_offset, offset = parse(buffer, offset, 'uint16')
        val, _ = parse_b(buffer, b3_offset)
        a1.append(val)
    a2, offset = parse(buffer, offset, 'int16')
    a3 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        a3_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_d(buffer, a3_offset)
        a3.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint16')
    b2, offset = parse_c(buffer, offset)
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint8')
    c2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        c2.append(val)
    c3, offset = parse(buffer, offset, 'float')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint8')
    d2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'double')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'double')
    d4 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'uint8')
        d4.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'\x95SOW\x00\x16\x00(\x009\x00K^\r\x00\x02\x00\x00\x00\xba\x19.\xe5\xb6'
            b"\xca\x00\x00\x00\x02\x00\x00\x00\x14\xbf~\xcd'J\xfd\x93\xf5\x14\xb3\x00"
            b'\x00\x00\x03\x00\x00\x00%>\xa2\xefw\t\xa0\x9c\x9ay\x00\x00\x00\x02'
            b"\x00\x00\x007\xbe\xa1'\x94\xa1\xc7\xd2\xa8\xf6\x06\x00\x00\x00\x03\x00\x00"
            b'\x00H\xbe\xe3e\xef?\xeb\x88@D\xb9\x9c0\xbf\xc26\x14X0Q\xd8\xbf\xe1'
            b'\x8d\xe3\x8d\n0\x9a?\xd7\xf4\x9ak\xa76\xc4a\x00\x00\x00\x04\x00\x00\x00Z\xbf'
            b'\xc5#\x10\x9b\xcd\xa0 s\x03\xaa?\xdc\xb2\xfbYH\xf3P\xbf\xc1m\\A/\xbd@?\xeb'
            b'\xa0\xce\n-UTi\x00\x00\x00\x03\x00\x00\x00\x8e\xbf\xcf-HF\xf9\xe1\xc0f'
            b'\x82\xf8\x00\x00\x00z\x00\x00\x00\xa6'))
