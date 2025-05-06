# 12 KISPYTHON CHEATSHEET

## _Библиотека возможных синтаксисов задачи._

## Оффсет и Порядок байт

Начальный оффсет всегда задается количеством сигнатур `ПЕРЕД` структурой А.

> Реализовать разбор двоичного формата данных. Данные начинаются с сигнатуры `0x59 0x49 0x52 0x50`, за которой следует
> структура A. `Порядок байт: от младшего к старшему`. Адреса указаны в виде смещений от начала данных. В решении
> предлагается использовать модуль struct.

Установка в коде может выглядеть по-разному, к примеру, можно сразу в функции main при вызове parse_a передавать
начальный оффсет.

```python
def main(data):
    result, _ = parse_a(data, 4)
    return result
```

Теперь о порядке байт:

- 'от младшего к старшему' - '<'
- 'от старшего к младшему' - '>'

Утсанавливается порядок байт в функции parse и передается в качестве аргумента по умолчанию, но, вообще его можно
передавать просто так, в зависимости от реализации вашей функции парса. Рекомендую использовать мой вариант, а не
типизированный, он более понятен для прочтения (ИМХО).

```python
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
```

## Возможные поля

Рекомендую просто собирать свой код как конструктор Лего из моих примеров.

### Поле - Кодировка

| Поле | Описание |
|------|----------|
| 1    | int64    |

```python
a1, offset = parse(buffer, offset, 'float')
```

### Структура

| Поле | Описание    |
|------|-------------|
| 2    | Структура B |

```python
a2, offset = parse_b(buffer, offset)
```

### Адресс (Кодировка) - Структуры

| Поле | Описание                   |
|------|----------------------------|
| 2    | Адрес (uint16) структуры B |

```python
a2_offset, offset = parse(buffer, offset, 'uint16')
a2, _ = parse_b(buffer, a2_offset)
```

### Массив (Кодировка), Размер (Размер)

| Поле | Описание               |
|------|------------------------|
| 2    | Массив uint8, размер 6 |

```python
d2 = []
for _ in range(6):
    val, offset = parse(buffer, offset, 'uint8')
    d2.append(val)
```

### Массив char, Размер (Размер)

| Поле | Описание              |
|------|-----------------------|
| 1    | Массив char, размер 7 |

```python
a1 = ''
for _ in range(7):
    val, offset = parse(buffer, offset, 'char')
    a1 += (val.decode())
```

### Массив Сруктур, Размер (Размер)

| Поле | Описание                    |
|------|-----------------------------|
| 4    | Массив структур F, размер 4 |

```python
a4 = []
for _ in range(4):
    a, offset = parse_f(buffer, offset)
    a4.append(a)
```

### Массив адрессов (Кодировка) Структур, Размер (Размер)

| Поле | Описание                                     |
|------|----------------------------------------------|
| 3    | Массив адресов (uint32) структур E, размер 8 |

```python
b3 = []
for _ in range(8):
    b3_offset, offset = parse(buffer, offset, 'uint16')
    val, _ = parse_e(buffer, b3_offset)
    b3.append(val)
```

### Размер (Кодировка) и Адрес (Кодировка) массива (Кодировка)

| Поле | Описание                                      |
|------|-----------------------------------------------|
| 2    | Размер (uint32) и адрес (uint16) массива int8 |

```python
b2 = []
array_siz, offset = parse(buffer, offset, 'uint32')
adr_offset, offset = parse(buffer, offset, 'uint16')
for _ in range(array_siz):
    val, adr_offset = parse(buffer, adr_offset, 'int8')
    b2.append(val)
```

### Размер (Кодировка) и Адрес (Кодировка) массива char

| Поле | Описание                                      |
|------|-----------------------------------------------|
| 1    | Размер (uint16) и адрес (uint32) массива char |

```python
b1 = ''
array_siz, offset = parse(buffer, offset, 'uint16')
adr_offset, offset = parse(buffer, offset, 'uint32')
for _ in range(array_siz):
    val, adr_offset = parse(buffer, adr_offset, 'char')
    b1 += (val.decode())
```

### Размер (Кодировка) и Адрес (Кодировка) массива Структур

| Поле | Описание                                            |
|------|-----------------------------------------------------|
| 3    | Размер (uint32) и адрес (uint16) массива структур D |

```python
c3 = []
array_siz, offset = parse(buffer, offset, 'uint32')
adr_offset, offset = parse(buffer, offset, 'uint16')
for _ in range(array_siz):
    val, adr_offset = parse_d(buffer, adr_offset)
    c3.append(val)
```

### Размер (Кодировка) и Адрес (Кодировка) массива Адрессов Стуктур

| Поле | Описание                                                            |
|------|---------------------------------------------------------------------|
| 3    | Размер (uint32) и адрес (uint16) массива адресов (uint8) структур D |

```python
a3 = []
array_size, offset = parse(buffer, offset, 'uint32')
adr_offset, offset = parse(buffer, offset, 'uint16')
for _ in range(array_size):
    a3_offset, adr_offset = parse(buffer, adr_offset, 'uint8')
    val, _ = parse_d(buffer, a3_offset)
    a3.append(val)
```
