"""
Work with comprehensions for lists, sets, dicts, and filtering them
"""
from math import factorial
from math import fmod
from pprint import pprint as pp


# returns a new list where its items are the len of each original items
def lists_comprehensions(items):
    return [len(item) for item in items]


# returns a new set
def sets_comprehensions(items):
    return {len(str(factorial(item))) for item in items}


# returns an inverse dict of the original one where key -> value, value -> key
def dict_comprehensions(dicts):
    return {key: value for value, key in dicts.items()}


# adding a filtering condition to a comprehension
def list_to_dict_with_filtering_comprehensions():
    return {(item, item * item): {1, item, item * item} for item in range(20) if fmod(item, 2)}


print(lists_comprehensions('Let\'s practice some lists comprehensions'.split()))
print(sets_comprehensions({4, 54, 634, 9, 32, 5, 2, 14, 6}))
pp(dict_comprehensions({1: 'red', 2: 'blue', 3: 'yellow'}))

pp(list_to_dict_with_filtering_comprehensions())
