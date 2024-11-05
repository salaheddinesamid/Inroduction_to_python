# Key : value

our_dict = {1 : "Messi", 2 : "Ronaldo" , 3 : "Maradona"}
students = {
    4422 : {
        "first_name" : "Salaheddine"
    },
    3362 : {
        "first_name" : "Alan"
    }
}
print(our_dict)  # This means that doesn't allow for duplicates.

for key in our_dict.keys():
    print(our_dict[key])

for key in students.keys():
    print(students[key]["first_name"])
