# ---------------------------------------------- Variables and data types
import csv
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
"""
Creating a variable in Python require few rules:
1- begin with a letter or underscore.
2- contains only letters, numbers or underscores.
3- be all lowercase.
4- words contains mutli-words should be separated with underscore.
5- descriptive
"""
# This variable holds information about my name:
my_name = "Salaheddine"  # String data type

# This variable holds information about my age:
my_age = 20  # Integer data type

# Accidental varibale creation
# Here we will try to update my_age

my_age = 29  # This will not throw an error

# --------------------------------------------------- Numbers:

# Integer:
my_integer = 100

# Float:
my_float = 12.2

# -------------------------------------------------- Strings:
# You can assign a string using "" or ''
my_string = "Hello from Python"
my_string_prime = 'Hello from Interpreter'

# Strings are immutable, means that once a string is created it cannot be modified.

# New line in string:
my_two_line = "Data science \nAI"

# --------------------Common string operations:
# 1- Get string length:
length = len(my_string)  # : 17

# 2- Get the index of a character:
index_of_P = my_string.index('P')  # : 11

# 3- Count occurence of a char:
occurence_of_l = my_string.count('l')  # : 2

# 4- to lower case:
upper_case = "HELLO EVERYONE"
lower_case = upper_case.lower()  # : hello everyone

# 5- String formatting:
my_self = "My name is :{}, and I'm : {} year old".format(my_name, my_age)  # : My name is :Salaheddine, and I'm : 29

# 6- Substring operations: You can extract parts of a string using slicing
# Syntax[start:end:step]

new_lower_case = lower_case[0:6]  # : hello

# 7- Join:

str1 = "I love"
str2 = "Programming is fun"
joined_string = "".join(str1)
# Replace "Programming" by "Python"
new_str_2 = str2.replace('fun', "hard")

# ------------------------------------ Collections:

# 1- Set:
"""
A set is an unordered collection of unique items, 
it's great for storing items where the order doesn't matter and duplicates are not allowed.
- Characteristics:
* Unordered.
* Unique.
* Mutable

- Methods:
* add()
* remove()
* clear()
"""

players_name = {"Messi", "Ronaldo", "Neymar"}

# Add new employee:
players_name.add("Casimero")  # : {"Casimero","Messi", "Ronaldo","Neymar"}

# Special type of Set : Frozenset, which is immutable:
frozen_players = frozenset({"Messi", "Ronaldo"})

# 2 List:
"""
List is a ordered collection of items, where duplicates are allowed.
It allows you to store items in a specific order and access it with index.

- Characteristics: 
* Ordered.
* Mutable.
* Allow duplicates.

- Methods:
* append(element)
* insert(i,element)
* remove(element)
* clear()
* count(element)
"""

# List of users:
users = [
    {
        "first_name": "John",
        "last_name": "Doe",
    },
    {
        "first_name": "Ronnie",
        "last_name": "Koile"
    }
]

# append(element):
"""
This method add new element to the list.
It requires one argument.
"""
new_user = {
    "first_name": "Salaheddine",
    "last_name": "Samid"
}
logging.info("Appending the new user:{} to the list".format(new_user))
users.append(new_user)
logging.info("Users list: {}".format(users))

# insert(index,element)
"""
This method allows you to add a new element within a specific position using index.
"""

special_user = {
    "first_name": "Elizabeth",
    "last_name": "Keen",
    "balance": 20000
}

logging.info("Inserting a special user: {}, at the top of the list.".format(special_user))
users.insert(0, special_user)
logging.info("User list: {}".format(users))

# 3 Dictionary:
"""
Dictionary is a collection type in Python, that are unordered and mutable.
It stores information as a key : value.
"""
countries = {
    '1': {
        'Country name': "Morocco",
        'Cities': [
            {
                'City name': "Casablanca"
            },
            {
                'City name': "Rabat"
            }
        ]
    },
    '2': {
        'Country name': "Germany",
        'Cities': [
            {
                'City name': "Berlin"
            },
            {
                'City name': "Munich"
            }
        ]
    }
}


def get_all_cities_by_country():
    target_country = input("Enter a name of any country: ")
    list_of_cities = []
    for key in countries:
        if target_country == countries[key]["Country name"]:
            for city in countries[key]['Cities']:
                list_of_cities.append(city['City name'])
        else:
            logging.info("No information available about: {}".format(target_country))
    print("The cities of {} are: {}".format(target_country, list_of_cities))


# Tuples:
"""
A tuple is a sequence of immutable objects.
They are created using parentheses instead of curly brackets.
It stores different data types.
"""

my_tuple = (1, 3.2, "John")

# -------------------------------------- Working with files:
"""
Python provides open() method, which takes at least two arguments: file_name, mode.
- Common modes:
* -r: opens file for reading.
* -w: opens file for writing, or creating new file.
* -a: appends data at the end of the file, without deleting any existing data.
* -x: creates a new file.

- The process of working with files: 
1. Open the file.
2. Performing operations.
3. Close the file.

- Why might File operations fail?
-> 1. File locks.
-> 2. Permission issues.
-> 3. Path error.
"""
path = "/Users/salaheddine/Downloads/Car_Specifications.csv"
try:
    with open(path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                logging.info(f'Column names are: {",".join(row)}')
            line_count += 1
except FileNotFoundError as r:
    logging.info(r)
