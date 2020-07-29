"""
    Negative indices are 1-based
    Slicing: a_list[start:stop] both start, and stop are optional
    copy: a_list.copy()
    index : a_list.index(arg)
    count: a_list.count(arg)
    del : remove an element by index (del a_list[index])
    insert : a_list.insert(index, obj)
    remove : a_list.remove(arg)
    reverse: a_list.reverse()
    sort: a_list.sort()
    reversed: returns an iterator, reversed(a_list)
    sorted: returns a new list, sorted(a_list)
"""

d = [1, -3, -9, 4, 6]

# access last element
print(d[-1])
print(d[len(d) - 1])

# access pre last element
print(d[-2])

# 0 = -0
print(d[0] == d[-0])

# slicing
slice_list = [43, 564, 23, 324, 233394844]
print(slice_list[1:3])
print(slice_list[:3])
print(slice_list[1:])

# we can use slice to create a copy of a list  // sallow copy
slice_to_copy_list = slice_list[:]
print(slice_to_copy_list is slice_list)  # should return False

# or we can use a_list.copy(list)  // sallow copy
copy_list = slice_list.copy()
print(copy_list is slice_list)

# The preferred way to copy a list is by using list(a_list)  // sallow copy
pref_list = list(slice_list)

# remove second element
del slice_list[1]
print('using del: ', slice_list)

# remove
slice_list.remove(324)
print('use remove: ', slice_list)

# insert
slice_list.insert(1, 111111)
print('Inserting at index[1]', slice_list)

# reverse
slice_list.reverse()
print('reverse: ', slice_list)

# sort
slice_list.sort()
print('sort: ', slice_list)

# sort with an optional arg
slice_list.sort(reverse=True)
print('sort with reverse = True: ', slice_list)

# sort with the 'key' optional arg, key should be a callable object
str_slice_list = 'Hey everyone, my name is Dania'.split(' ')
str_slice_list.sort(key=len)
' '.join(str_slice_list)
print('sort with key=len: ', str_slice_list)

# sorted
y = sorted([4, 1, 0])
print('using sorted:', y)

# reversed
q = reversed(y)
print('using reserved: ', q)
r = list(q)
print(r)
