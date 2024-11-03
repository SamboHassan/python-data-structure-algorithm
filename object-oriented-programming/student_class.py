from package_employee import person
import vector

haladu = person.Person("Umar")
print(haladu)


# DATA
student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


# LOGIC
def average(sequence):
    return sum(sequence) / len(sequence)


# OPERATION ON DATA
print(average(student["grades"]))

# But wouldn't it be nice if we could...
# print(student.average()) ?


# CLASS BUNDLE DATA AND OPERATION ON DATA
class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (89, 90, 93, 78, 90)

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student()
print(student.average())
# Identical to Student.average(student)


# -- Parameters in __init__ --


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (36, 67, 90, 100, 100))
print(student.average())

# -- Remember *args ? --


class Student:
    def __init__(self, name, *grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", 36, 67, 90, 100, 100)
print(student.average())


class Dog:
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF THE CLASS BLUEPRINT
    species = "mammals"

    def __init__(self, breed, name, spots):
        # we take in the argument
        # assign it using self.attr_name
        self.breed = breed
        self.name_attr = name  # same as above
        self.spots = spots  # Expect boolean TRUE/FALSE

    def back(self):
        return "Woffs"


my_dog = Dog(breed="Lab", name="Sam", spots=False)

print(my_dog.species)
# even though we have not define it,
# it will always be available to us
print(my_dog.name_attr)
print(my_dog.back())
