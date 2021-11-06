import sys
import re


def translator(txt: str) -> str:
    """
    text to "Двуликий код" converter
    """
    template = 'двуликий'
    result = ''

    encode = 'utf8'
    if bool(re.search('[\u0400-\u04FF]', txt)):
        encode = 'cp1251'  # for cyrillic characters

    for ch in txt:
        bits = bin(int.from_bytes(ch.encode(encode), sys.byteorder))[2:].zfill(8)
        for i in range(8):
            if bits[i] == '1':
                result += template[i].upper()
            else:
                result += template[i]
        result += ' '

    return result.rstrip()


if __name__ == '__main__':
    print(translator('Hi'))
    print(translator('123'))
    print(translator('Hello World'))
    print(translator('Привет'))
    print(translator('Привiт!'))
