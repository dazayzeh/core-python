"""
    dictionary
"""
from pprint import pprint as pp

# define a dict
dictionary = {'a': 1, 'b': 2, 'c': 3}
sec_dict = dict(s=0, e=9, r=10)
pp(dictionary)
pp(sec_dict)

# update
dictionary.update(sec_dict)
pp(dictionary)

# iterate
for key, val in dictionary.items():
    print(f'key ={key}, val ={val}')

for key in dictionary.keys():
    print(' key: ', key)

for val in dictionary.values():
    print(' val: ', val)
