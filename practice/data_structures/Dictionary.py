# Use of dictionary:
"""
If you are storing data that needs some kind of mapping and you need to access it fast
, then using a dictionary would be wise.
"""

my_dict = {0: "Aby", 1: "Larry", 2: "Ronnie"}
print(my_dict)

my_iter_dict = iter(my_dict)
for key in my_dict.keys():
    print(next(my_iter_dict))