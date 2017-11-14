class Person:

    def __init__(self, name, ID, Department):
        self.Personname = name
        self.PersonID = ID
        self.PersonDepartment = Department 
    def __str__(self):
        return self.Personname+ " " + self.PersonDepartment+ ", " + str(self.PersonID)

class Employee(Person):

    def __init__(self, name, ID, Department, Title):
        super().__init__(name, ID, Department)

        self.StaffTitle = Title
    def __str__(self):
        return super().__str__() + ", " +  self.StaffTitle


x = Employee("Susan Meyers", 47899, "Accounting", "Vice president")
y = Employee("Marke Jones", 39119, "IT", "programming")
z = Employee("Joy Rogers", 81774, "Manufacturing", "Engineering")

print(x)
print(y)
print(z)
