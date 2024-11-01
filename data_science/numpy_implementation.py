import numpy

my_array = numpy.array([0,5,10,15,20,25])

#Print the data type
print(type(my_array))

#Multiply the array by 5 and assign it to new array
new_array = my_array * 5


print("First array:" + str(my_array))
print("Second array:" + str(new_array))

# Compute and print the sum:
print("First array sum= " + str(my_array.sum()))
print("Second array sum= " + str(my_array.sum()))