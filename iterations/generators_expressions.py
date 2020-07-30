"""
Mix between comprehensions and lazy evaluation
"""

# generator expression
g_exp = (x * x for x in range(1, 10000000))

# create a list from the generator
g_list = list(g_exp)[-10:]
print(f"g_list =: {g_list}")

# use dictionary expression to create a dict from the list
g_dict = {list_item: 'val' for list_item in g_list}
print(g_dict)

# anther generator expression
print(sum(x * 3 for x in range(100) if x % 2 == 0))
