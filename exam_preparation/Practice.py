# ---------------------- Data structures:

# List:
var = 20
print(type(var))


def filtering(list):
    """

    Args:
        list:

    Returns: List containing only numbers.

    """
    int_list = []
    for i in range(0, len(list)):
        if type(list[i]) == int:
            int_list.append(list[i])
    return int_list


given_list = ["String", 20.3, 10, 'l']

# ------------------- Dictionaries:
def add_new(elements,key,element):
    """

    Args:
        elements: Original dictionary.
        key: The key of the element.
        element:

    Returns: New dictionary with a new element.

    """
    elements[key] = element
    return elements

dictionary = {"Hair color" : "Green", "Weight" : 190}

def dict_iteration(elem):
    """

    Args:
        elem:

    Returns: Every element in the dictionary

    """
    for key in elem.keys():
        print(elem[key])

# -------------------- Set:

a_set = {10,20,13,24}
b_set = {10,9,24,2}
print(a_set.union(b_set))
print(a_set.intersection(b_set))

duplicates = [3,4,2,3,4]
def remove_duplicates(dup):
    """

    Args:
        dup: Duplicates elements.

    Returns: Non duplicate elements using a set.

    """
    unique = {item for item in dup}
    return unique

players_name = {"Messi", "Ronaldo", "Neymar"}
empty_set = set()
empty_set.add(20)
print(empty_set)

# ------------------ Functions:

students = { 1: {
    "name" : "John pil",
    "age" : 20
},
    2 : {
        "name" : "Ronnie Kolemman",
        "age" : 28
    }
}
def return_max_age(dictionary):
    """

    Args:
        dictionary: Takes a  dictionary of students.

    Returns: The oldest student.

    """
    max_age = 0

    for key in dictionary.keys():
        student = dictionary[key]
        if student["age"] >= max_age:
            max_age = student["age"]


    return max_age

print(return_max_age(students))