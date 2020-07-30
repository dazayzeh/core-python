"""
Shows how to use :
    f-string , join, split, partition

"""

# f-string
import datetime
import math

val = 60
print(f'the value is {val}')

print(f'the current time is {datetime.datetime.now().isoformat()}.')

print(f'Math has: pi={math.pi}, e={math.e}')
print(f'Math has pi={math.pi:.3f}, e={math.e:.3f}')

# str.join() inserts a separator between a collection of strings
# returns a string
# call join on the separator of the string

colors = ' '.join(['red', 'blue', 'black'])
print(type(colors))
print(colors)

# str.split(), returns a list
split_colors = colors.split(" ")
print(type(split_colors))
print(split_colors)

# str_partition() separate the string into three parts
# 1. the part before  2. separator  3. the part after
# returns a tuple
str_partition = "separating a string".partition('a')
print(type(str_partition))
print(str_partition)

start_point, _, end_point = 'Berlin:Hamburg'.partition(':')
print(start_point, end_point)
