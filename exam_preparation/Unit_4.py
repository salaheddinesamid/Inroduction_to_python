# ----------------------------------------------- Functions ----------------------------------------------------- #

"""
Function is a set of reusable block of code that can be called whenever are needed.
When a function is called, Python jumps to the function's code block, executes it
and return to the point right after the function was called.
"""
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
# -------------------- Creating a custom function:
"""
To create a custom function, the following steps must be followed:
1- "def" keyword.
2- the name of the function.
3- Parentheses.
4- colon ":"
"""


# Example of a custom function:
def occurrence_counting(string, letter):
    occurrence = 0
    for char in string:
        if letter == char:
            occurrence += 1
    print("The letter: {} ".format(letter) + "had repeated: {} ".format(occurrence) + "time")


occurrence_counting("Hello", 'l')

# ------------------------ Scope:
"""
Scope determines the visibility of variables and functions within a program.
A variable or a function is said to be in scope, if the interpreter can recognize it in a given line of code.
"""

# 1- Local variable:
"""
Local variables: are variables or functions that are defined inside of of a function and only be accessible within it.
"""


def my_function():
    local_variable = 3
    # Here the variable "local_variable" is defined inside the function and can be accessed only within it.
    print(local_variable)


# If we try to call that variable from outside the function, the program will throw an error:
try:
    print(local_variable)
except NameError:
    print("Variable not found")

# 2- Global variable:
"""
Global variable : are variables or functions that are defined outside the function and are accessible throughout the entire program.
"""
global_variable = 100
logging.info("Defining global_variable: {}".format(global_variable))


def another_function():
    print(global_variable)
    logging.info("Accessing the variable inside the function.")


logging.info("Accessing the variable outside the function.")

# 3- Nested scope:
"""Nested scope: variables and functions that are defined within a nested function are only accessible within that 
specific function."""


def main_function():
    def nested_func():
        nested_variable = 20
        print(nested_variable)

    nested_func()


# ------------------------ Arguments:

"""
Arguments : allow the function to accept external data.
They are also called parameters.
"""


# This function takes two arguments (x,y) and return their sum:
def my_func(x, y):
    return x + y


my_func(5, 10)

"""
Attention : The number of arguments provided during the function call must match the number of parameters defined in the 
function.

There are two types of arguments:
1- Positional arguments : These are matched to parameters based on their position in the function call.
2- Named arguments : Arguments can be specified by name, allowing them to be provided in any order.
"""


# 1- Positional arguments:

def positional_args(a, b):
    logging.info("The value of a = {}".format(a))
    logging.info("The value of b = {}".format(b))


# 2- Named arguments:

def named_args(name, phone):
    logging.info("Hello {}".format(name) + ", your phone number is: {}".format(phone))



# --------------------- Default arguments:
"""
Default argument : provide present value if the caller doesn't supply one.
Rules for default arguments : 
* Default arguments must appear on the right side of the parameter.
* You can not place a parameter with a default before one without a default.
"""


def default_args(y, x = 30): # The default parameter must appear at the right!
    return y * x

# ----------------------- Return values:
"""
Functions can also send back results to the caller using return keyword.
The return statement ends the function's execution and sends a value back where the function was called.
"""

def return_max_num(arr):
    max = 0
    for item in arr:
        if item >= max:
            max = item
    return max

def sort_array(arr):
    l = len(arr)
    for index in range(0,l):
        toInsert = arr[index]
        j = index
        while j > 0:
            if toInsert > arr[j - 1]:
                break
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = toInsert

# Return multiple values:
"""
Functions can return multiple values by separating them with commas.
"""
def mutli_return(x,y):
    return x*2,y*2

a , b = mutli_return(2,4) # 'a' will hold the value of x*2 and 'y' will hold the value of y*2



def convert_my_str():
    try:
        user_input = input("Please enter a value:")
        data_type = input("In which data type do you want to convert it to? ")
        new_user_input = None
        if data_type == "int":
            new_user_input = int(user_input)
        elif data_type == "float":
            new_user_input = float(user_input)

        logging.info("The conversion went successfully, {}".format(new_user_input))
    except ValueError as v:
        logging.info(v)


convert_my_str()