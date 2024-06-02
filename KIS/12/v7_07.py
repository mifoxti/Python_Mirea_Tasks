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
    a1 = ''
    for _ in range(4):
        val, offset = parse(buffer, offset, 'char')
        a1 += (val.decode())
    a2 = []
    for _ in range(2):
        a, offset = parse_b(buffer, offset)
        a2.append(a)
    a3, offset = parse_c(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint16')
    b2, offset = parse(buffer, offset, 'double')
    b3, offset = parse(buffer, offset, 'uint8')
    b4, offset = parse(buffer, offset, 'int16')
    return {'B1': b1, 'B2': b2, 'B3': b3,
            'B4': b4}, offset


def parse_c(buffer, offset):
    c1 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'float')
        c1.append(val)
    c2_offset, offset = parse(buffer, offset, 'uint16')
    c2, _ = parse_d(buffer, c2_offset)
    c3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'double')
        c3.append(val)
    c4, offset = parse(buffer, offset, 'uint32')
    c5, offset = parse(buffer, offset, 'uint16')
    return {'C1': c1, 'C2': c2, 'C3': c3,
            'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint8')
    d2 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'uint16')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'uint8')
    d4, offset = parse(buffer, offset, 'uint8')
    d5, offset = parse(buffer, offset, 'int32')
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4, 'D5': d5}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b"MME\xe1ughfw\x9d\xba.M\xdc\xe0\xec\xeb\xbf\x89\xe6\x89',(\x97\xa6\xe2\x0f"
            b'\xd0\xc8\xbf\xfc\x80\x00\tB*?.\x81\xb8\xbb\x80[\x18\xbf>\x00\x02\x00\x00\x00'
            b'O\x00\x00\x00\x9d\x93*\x10@\x19\xc7\x18\x93v_L\xc1\x8c\xffe\xb1\xf0\x149'
            b'\xac\x91\xa7v6\xdc\t \xee\xed\xbf(\rs\xf9\xe0+\xcf\xbf'))
