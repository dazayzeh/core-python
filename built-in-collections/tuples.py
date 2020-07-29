"""
Tuples are zero indexed immutable sequences of arbitrary objects

"""

# defeine a tuple
tuple_test = ("Germany", 23.09, 1)
# or
second_tuple = "Hamburg", 'python', 4, 9, 1
print("second tuple type", type(second_tuple))

# access first item
print(tuple_test[0])

# length
print(len(tuple_test))

# loop over a tuple's items
for item in tuple_test:
    print(item)

# add new items to a tuple
tuple_test_add = tuple_test + ('hey', 4.5)
print(tuple_test_add)
# duplicate tuple values
tuple_test_duplicate = tuple_test * 3
print(tuple_test_duplicate)

# nested tuples
nested_tuples = ((34, 23), (1, 9), (0.8, 0.4))

# print nested tuples items per line
for row in nested_tuples:
    for col in row:
        print(col)

# access nested tuples items
print(nested_tuples[0][1])

# initiate empty tuple
empty_tuple = ()
print(type(empty_tuple))

# a tuple with one item
single_item_tuple = (3,)

# a tuple from other data types
tuple_list = tuple([8, 4, 5, 3])
tuple_str = tuple('Germany')
print('tuple list=', tuple_list)
print('tuple from a string=', tuple_str)


# returning multiple values as a tuple from a function
def minmax(items):
    return min(items), max(items)


print(type(minmax([4, 8, 9, 5, 3, 5])))

# Tuple unpacking
min_val, max_val = minmax([1, 2, 3, 4, 5, 6, 10])
print('min = ', min_val, ' ,max = ', max_val)

# nested tuple unpacking
(a, (b, (r, d))) = (2, (5.4, (9, 11)))
print(a, b, r, d)

# value in tuple or not
print(4 in (4, 5, 6, 2))
print(8 not in (4, 23, 2, 1))
