# -*- coding: utf-8 -*-

from hypothesis import given
from hypothesis.strategies import text


def rle_encode(s):
    if not s:
        return ''

    encoded = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += str(count) + s[i - 1]
            count = 1
    encoded += str(count) + s[-1]
    return encoded


def rle_decode(s):
    decoded = ''
    i = 0
    while i < len(s):
        count = int(s[i])
        decoded += s[i + 1] * count
        i += 2
    return decoded


# Генерируем случайные строки для тестирования
string_strategy = text()


@given(string_strategy)
def test_rle_encode_decode(s):
    encoded = rle_encode(s)
    decoded = rle_decode(encoded)
    assert decoded == s


test_rle_encode_decode()
