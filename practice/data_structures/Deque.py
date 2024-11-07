"""
If you want to create a queue or and stack, then consider using deque.
"""

from collections import deque

# Make a deque:
deq = deque("abcdefg")

#Iter over the deque's element:
my_list = [element for element in deq]
print(my_list)