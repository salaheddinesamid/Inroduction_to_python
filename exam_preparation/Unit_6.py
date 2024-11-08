# ------------------------------------------------ Modules and packages ----------------------------------------#
"""
In Python, a module is simply a file containing Python code that can be reused in other programs.
- Modules allow you to organize code into separate files.
"""
import math
import numpy
import matplotlib.pyplot as plt
import scipy
import pandas

# ------------------ Usage:
"""
- The 'import' feature in Python allows developers to access functions, classes and variables from other Python files.
- This feature is useful for:
* Creating separation code.
* Facilitating code reuse across different applications.
* Accessing functionality from external libraries.
"""

# ------------------ Namespaces:
"""
- Namespace : is a container for variable and function name. It organizes names to prevent conflicts by keeping them
distinct based on their usage and scope.
- Python organizes namespaces into three main types:
1- Built-in namespace : contains all built-in functions and exceptions, like "print() , len()"...
2- Global namespace : contains all variables and functions defined at the top level of a module, and accessible through 
the program.
3- Local namespace : contains variables and functions defined within a function, accessible only within that function.
- Namespace allows different parts of the code to use the same name without conflict, based on where that name is 
defined.
"""


# Example:
def floor(x):
    print("Floor: {}".format(x))


my_variable = 20.23

floor(my_variable)
# Using math.floor instead of calling floor() to avoid conflicts.
print(math.floor(my_variable))

# ----------------- Documentation
"""
- Python emphasize readability, and one way to enhance it is through comments and docstrings.
"""
# 1- Comments:
"""
- In Python, comments start with "#" symbol and are ignored by the interpreter.
- They help explain code logic and intent, guiding others to understand the purpose of specific lines of code 
or functions.
"""

# 2- Docstrings:
"""
- Python provides a built-in function documentation method called 'docstring'.
- A docstrings is a string placed within triple quotes at the beginning of a function, or module or class to describe
its purpose.
- Unlike comments, docstrings can be retrieved at runtime and are more commonly used for generating external 
documentation.
"""

# ------------------ Popular Data science packages

"""
- Python offers several powerful libraries for data science, including:
* Numpy : is a foundational for data science. It provides efficient data types and functions for array computations and 
support large data sets with more speed and flexibility.
  -> Key features:
  1- Efficient data storage and handling with optimized array structures.
  2- High-speed computation.
  3- Robust suite of statistical functions.
* Matplotlib : is a versatile library for creating a wide range of plots and charts. Its functions make it easy to 
virtualize data with plots like charts, graphs...
  -> Key features:
  1- Extensive customization options for plots.
  2- Compatible with Numpy arrays, making it easy to plot data.
  
* SciPy : builds on NumPy and provides functions for scientific and engineering computations, including linear Algebra...
  -> Key features:
  1- Support advanced Mathematical functions.
  2- Ideal for computing tasks.
  
* Pandas : is invaluable for data manipulation and analysis. It introduces high-performance data structures such as
DataFrame, 2D arrays for managing data.
  -> Key features:
  1- Efficient data handling with structures like DataFrames.
  2- Simplified data import from format like (csv, json...).
  3- Built-in functions for filtering, storing and data manipulation.
"""


# --------------------- NumPy
# Initializing an array:
def numpy_example():
    my_array = numpy.array([0, 5, 10, 15, 20, 25])

    # Print the data type
    print(type(my_array))

    # Multiply the array by 5 and assign it to new array
    new_array = my_array * 5

    print("First array:" + str(my_array))
    print("Second array:" + str(new_array))

    # Compute and print the sum:
    print("First array sum= " + str(my_array.sum()))
    print("Second array sum= " + str(my_array.sum()))
    print("Maximum number is : " + str(my_array.max()))
numpy_example()
# -------------------- Matplotlib:

def matplotlib_example():
    # Simple plot:
    my_array = numpy.array([1, 10, 5, 4, 19, 0, 2, 8])
    plt.plot(my_array)
    plt.show()

    # Simple pie chart:

    categories = 'Cars', 'Trucks', 'SUVs', 'Motorcycles', "Minivans"
    quantities = [250, 150, 175, 70, 90]
    fig, axl = plt.subplots()
    axl.pie(quantities, labels=categories, autopct='%1.1f%%',
            shadow=True, startangle=90)

    axl.axis('equal')
    plt.show()

    # Scipy:
    my_data = scipy.stats.norm.rvs(size=500)
    plt.hist(my_data, bins=50)
    plt.show()


# --------------- Pandas:

def reading_csv():
    path = "/Users/salaheddine/Downloads/Car_Specifications.csv"
    car_data = pandas.read_csv(path)
    car_data.head()

my_numpy_array = numpy.array([2,30,12,3,4])
multi_dimensional_array = numpy.array([[1,3,4],[9,2,4]])
reversed_multi_array = []
print(my_numpy_array[1::3])
multiplied_array = my_numpy_array * 3
divided_array = my_numpy_array / 2
print(multiplied_array)
print(divided_array)
print(multi_dimensional_array)
print('The size of the array: {} is: {}'.format(multi_dimensional_array,numpy.size(multi_dimensional_array)))

print(multi_dimensional_array.reshape(3,2))
# Printing rows of an multi-dimensional array:

def access_multi_dim_array():
    def way_one():
        for row in multi_dimensional_array:
            for col in row:
                print(col)

    def way_two():
        for i in range(0,len(multi_dimensional_array)):
            for j in range(0,len(multi_dimensional_array[i])):
                print(multi_dimensional_array[i][j])


# Matrix A:
A = numpy.array([[1,6,7],[2,7,9]])
B = numpy.array([[3,7],[9,6],[2,1]])

C = A + B
D = numpy.matmul(A,B)

print(numpy.shape(A))
print(numpy.shape(B))

print(D)