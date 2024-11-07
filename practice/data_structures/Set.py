# Use Sets for Speed:
"""
Sets are fundamental data structures in Python. The main benefit of using sets is speed.
- They don't allow for duplicates.
- You can access set elements in O(1), since they use hashtable.
- You can't access the sets using the index.
"""
data = {"first", "second", "third", "fourth", "fifth"}
if "first" in data:
    print("Found")

# Example:
"""
Let's look to an example where sets are useful and can help make sure your data is not being duplicated.
"""
new_data = ["first", "second", 'third',"third"]
set_data = set(new_data)
print(set_data)