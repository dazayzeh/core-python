
import sys

DIGIT_MAP = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def convert(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += str(DIGIT_MAP[token])
        return int(number)
    except (KeyError, TypeError) as e:
        print(f'conversion failed {e!r}', file=sys.stderr)
        raise
    finally:
        print('finally has been reached anyway')


print(convert('one two three'.split()))
print(convert(' what\'s up?'.split()))
