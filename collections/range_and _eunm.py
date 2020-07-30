"""
 range() Signature

    range(stop)
    range(start, stop)
    range(start, stop, step)

 enumerate() : constructs an iterable of (index, value) tuple
"""

# range()
for i in range(5):
    print(i)

print('create a list out of a range:')
print(list(range(1, 10, 2)))

# enumerate
lis = [36, 45, 64, 000, 23432424]
for enu in enumerate(lis):
    print(enu)

for index, val in enumerate(lis):
    print(f'index = {index}, val = {val}')
