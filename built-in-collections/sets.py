"""

A set is an unordered collection with no duplicate elements.

"""
# define a set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
sec_basket = set(['mint', 'tea', 'coffee'])
print(basket)
print(sec_basket)

# add to a set
basket.add('beans')
print(basket)

# remove
basket.remove('beans')
print(basket)

# discard // won't cause an error if the item doesn't exist
basket.discard('lol')

# mathematical operations
a = set('abcdefghiijj')
b = set('jhfdzxcvb')

# letters in a but not in b
print(a)

# unique letters in a
print(a - b)

# letters in a or b or both
print(a | b)

# letters in both a and b
print(a & b)

# letters in a or b but not both
print(a ^ b)
