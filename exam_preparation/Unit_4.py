# ----------------------------------------------- Functions ----------------------------------------------------- #

"""
Function is a set of reusable block of code that can be called whenever are needed.
When a function is called, Python jumps to the function's code block, executes it
and return to the point right after the function was called.
"""
import logging

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
Local variables: are variables or functions that are defined inside of of a function and only accessible within it.
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
Global variable : are variables or functions that are defined 
outside the function and are accessible throughout the entire program.
"""
global_variable = 100
logging.info("Defining global_variable: {}".format(global_variable))


def another_function():
    print(global_variable)
    logging.info("Accessing the variable inside the function.")


logging.info("Accessing the variable outside the function.")
