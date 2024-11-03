# ------------------------------------- Errors and Exception handling -----------------------------------------#

# -------------------------- Errors:
"""
There are several types of errors:
1- Syntax Error : this error occurs when code violates Python's structural rules.
"""
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
# 1- Sytnax error:
"""
When a syntax error occurs, Python halts execution and provide a detailed error message:
* Error type.
* Line number.
* Error location.
Error messages point to the most likely problem area, but they are not always precise.
"""


def syntax_error_test():
    logging.info("Here we will try to throw a syntax error")
    try:
        variable = 18
        if variable >= 18:
            print("Yes")
    except SyntaxError:
        logging.info("Error detected")


# ----------------------- Exception:
"""
Exception : an exception is an error that occurs during the execution and disrupt the flow of the program.
Common types of exceptions : 
* ZeroDivisionError : Raised when dividing a number by zero.
* FileNotFoundError : Occurs when attempting to access a non-existent file.
* TypeError : Triggered when an operation is applied to an inappropriate data type.
"""


def divide_by():
    number_to_divide = int(input("Enter a number: "))
    number_to_divide_by = int(input("Enter a number to divide by: "))
    try:
        return number_to_divide / number_to_divide_by
    except ZeroDivisionError as e:
        logging.info(str(e))
"""
To prevent applications from crashing when an exception occurs, Python provides the "try/except" structure for handling 
exceptions.
* try : contains the code that may produce an exception.
* except : captures and handles the exception if it occurs.

Python allows programmer to handle multiple exceptions within a single try block by specifying separate except blocks
for each exception type.
"""
# Using finally:
"""
The finally clause provides a way to ensure that certain code executes after try/except block, regardless of whether an 
exception occurred.
"""

def reading_txt_file(path):
    try:
        with open(path, "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError as e:
        logging.info("An error occurred : {}".format(e))
    except ValueError as v_e:
        logging.info("An error occured : {}".format(v_e))
    finally:
        print("Closing file...")
        file.close()

# ------------------------- Logs:
"""
- Another type of error, called "logical error", happens when code is syntactically correct but doesn't produce the
desired results.

- Logical errors are challenging to catch because they don't generate error messages.

- Logging, allows developers to track key points of a program's execution and see detailed information.

- To use logging in Python :
* First, we import the logging library by adding 'import logging'.
* Python logging has different level of severity: 
  1- debug : For detailed diagnostic information.
  2- info : for general information on program execution.
  3- warning : for warnings about unexpected events that are not critical.
"""
