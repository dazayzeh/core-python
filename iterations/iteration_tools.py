from itertools import *
from math import *

# islice() perform lazy slicing of any iterator
# count() infinite count
# using generator expression with islice
iterable = islice((x * x for x in count() if fmod(x, 2)), 1000)
print(list(iterable)[-10:])

# remember generators create always a new object so we can't here usr iterable again
print(sum(islice((x * x for x in count() if fmod(x, 2)), 1000)))

# Using any() and all()
print(any(fmod(item, 3) for item in count()))
print(all(name == name.title() for name in ['London', 'Hamburg', 'Berlin']))

# zip
week_days = (11, 22, 33, 44, 55, 66, 77)
week_numbers = (1, 2, 3, 4, 5, 6, 7)

for tmps in zip(week_numbers, week_days):
    print(f'min = {min(tmps)}, max = {max(tmps)} ')

for num, day in zip(week_numbers, week_days):
    print(f'num = {num}, day = {day}')

# check if all temp are below 30 using chain(), all() and generator expression
tmp1 = [12, 23, 25, 27, 29]
tmp2 = [1, 1, 1]
tmp3 = [8, 4]

print(all(tmp <= 30 for tmp in chain(tmp1, tmp2, tmp3)))
