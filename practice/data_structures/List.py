# List:
"""
List stores elements in an ordered way and allows for duplicates.
- You can access elements using index.
- append()
- insert(i,element)
- pop()
- remove(element)
- clear()
"""
my_list = ["Abe","Larry","Adams","John"]
"""
my_list.append("Ronnie")
print(my_list)
my_list.insert(0,"Mathew")
print(my_list)
my_list.clear()
print(my_list)
"""

# Using zip:
"""
- When you have two lists and you want to process them in parallel,
consider using zip.
"""

def get_user_id():
    ids = [2, 33, 88, 189, 812]
    my_list = ["Abe", "Larry", "Adams", "John"]
    user_ids = []
    for usr,id in zip(my_list, ids):
        user_ids.append((usr, id))
    print(user_ids)


get_user_id()