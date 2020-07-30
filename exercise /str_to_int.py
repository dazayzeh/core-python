"""

Converts a string to its corresponding int values

"""

import sys


def convert(s):
    try:
        digit_num = ''
        for token in s:
            number = sorted(set(token))
            for item in number:
                digit_num += str(ord(item))
        return digit_num
    except () as e:
        print(f'conversion failed {e!r}', file=sys.stderr)
        raise



r = convert('Hey nice to meet you'.split(' '))
print(r)
