# -------------------------------------------------------- Unit 3: Statements -----------------------------------_#
import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
# ------------------ Assignment and Expressions:
"""
There are several assignment techniques for assigning a value to a variable, such as:
* = : assigns value on the right to the variable on the left.
* += : takes the value stored, adds the value on the right to it, and assign the value back.
* -= : takes the value stored, subtracts the value on the right to it, and assign the value back.
...
"""

# Assign the value 20 to the variable my_age:
my_age = 20

# Increase the value by 2:
my_age += 2

# Chained assignment: We can assign one value to multiple variables:
a = b = c = 10  # The value: 10 will be assigned to a,b and c.


# ---------------- Conditional Statements:

"""
Conditional statements helps your program to make decisions based on specific conditions.
If: Checks whether an expression is true.
Elif: Checks whether another expression is true.
Else: Check whether no expression is true.
"""

# Here we will write a program that takes user age and return "You are adult" or " You are not adult":

def age_check():
    age = int(input("Please enter your age: "))
    logging.info("The program takes the user's age")
    if age >= 18:
        logging.info("Verifying whether the age is more than or equal to 18")
        print("You are adult.")
    else:
        print("You are not adult.")

"""
Statements : are lines of code that can be executed by the interpreter.
Expression : are sections of code that the interpreter evaluates a value.
Boolean expressions : evaluates to either True or False.
"""

# ----------------------------- Loops:

# 1- For loop:
"""
range() function, takes at least one argument, and generates a sequence of numbers.
It has three parameters:
* start (optional): starting of the sequence.
* stop : ending point.
* step (optional) : how much increment.
"""
def for_loop_test():
    logging.info("This is an example of how range function works.")
    for item in range(0, 10):
        logging.info(f'items are: {",".join(str(item))}')

# Here is an example of a for loop:

def player_iteration():
    players = ["Kyle", "Morgan", "Jordan"]
    for i in range(0, len(players)):
        print(players[i])

# 2- While loop:


"""
While loop is another Python looping, that repeatedly executes as long as a specific condition is True.
"""
def while_loop_test():
     j = 9
     while j > 0:
         print("Hello from while loop")
         j -= 1

# Avoiding infinite loop:

"""
1- Break keyword allows you to exit the loop early, regardless of whether the condition is still True.
2- Continue keyword allows you to skip the current iteration, without exiting the loop entirely.
"""

def for_loop_with_break():
    my_players = ["Ronaldo","Messi","Neymar"]
    l = len(my_players)

    for i in range(0,l):
        if my_players[i] == "Messi":
            print("The best player is found!")
            break
# 3- Iterators and comprehensions:

"""
* Iterators: an iterator allows you to iterate over values within a list, tuple and dictionaries.
* Comprehensions provide a concise way to generate new lists by applying operations to each element of an existing iterable.
"""

# Example of an iterator:
def iterate_over_a_list():
    my_list = [1, 6, 8, 10, 20]
    my_iterator = iter(my_list)

    # By calling next() method, you can retrieve each element from the list sequentially:
    l = len(my_list)

    while l > 0:
        print(next(my_iterator))
        l -= 1

def iterate_over_a_dictionary():
    my_dict = {
        '1':{
        "first_name" : "John",
        "last_name" : "Doe",
    },
        '2' : {
            "first_name" : "Ronnie",
            "last_name" : "Kyle"
        }
    }
    my_iterator = iter(my_dict)
    for key in my_dict.keys():
        print(next(my_iterator))

# Example of comprehension:

my_numbers = [2, 3, 7, 8, 9]
logging.info("Initializing a list: {}".format(my_numbers))
double_number = [x*2 for x in my_numbers]
logging.info("Double each element and then: {}".format(double_number))

