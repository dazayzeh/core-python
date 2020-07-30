"""
Iterator protocol

"""


def iterate(items):
    iterator = iter(items)
    while True:
        try:
            item = next(iterator)
        except StopIteration as e:
            break  # to catch the exception use : raise ValueError(f'finished iterating with {e!r}')
        else:
            print(item)


iterate(['A', 'B', 'C'])
