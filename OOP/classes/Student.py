class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_student_info(self):
        return "Current user is: {}, and he/she is: {}".format(self.name,self.age)



class Employee(Person):
    ROLES = ("Supervisor","Manager","CEO","Founder")

    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department
        self.age = None
        self._age_last_calculated = None

    def __str__(self):
        return ("Name: " + self.name + "\nDepartment: " + self.department)