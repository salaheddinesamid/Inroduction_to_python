data = {
    "first1", "second", "third", "fourth"
}


# This function search for an element in a set
def find_element(set):
    element_exists = False
    for item in set:
        if item == "first":
            element_exists = True
            break
    if element_exists:
        print("Element found")
    else:
        print("Sorry, not found")





def generate_full_names():
    users = {
        '1267': {
            'first_name': "Larry",
            'last_name': "Page"
        },
        '2343': {
            'first_name': "John",
            'last_name': "Freedom"
        }
    }
    ids = set(users.keys())
    # print(ids)
    full_names = []
    for user in users.values():
        full_names.append(user["first_name"] + " " + user["last_name"])
# Using zip

def get_user_salary():
    users = ["Abe","Larry","Adams","John","Sumit","Adward"]
    salary = ["2M","1M","60K","30K"]
    user_salaries = []

    for usr,slr in zip(users,salary):
        try:
            user_salaries.append(usr,slr)

        except IndexError:
            user_salaries.append(usr,"No data available")

    print(user_salaries)

get_user_salary()