class Person:
    """docstring for Person"""

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return f"Person: {self.name}, pay: {self.pay}"


class Manager(Person):
    def __init__(self, name, pay):  # Redefine constructor
        Person.__init__(self, name, "mgr", pay)

    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent + bonus)


# Other common coding pattern involves nesting objects inside
# each other to build up composites.
# i.e EMBEDDING A Person instead of inheriting from it.


class Manager2:
    def __init__(self, name, pay):
        self.person = Person(name, "mgr", pay)  # Embed a person object

    def giveRaise(self, percent, bonus=0.10):
        self.person.giveRaise(percent + bonus)  # Intercept and delegate

    # Delete all the attrs
    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __str__(self):
        return str(self.person)  # Must overload again


# This alternative is a general coding pattern usualy known as
# DELEGATION --- a composite-based structure that manages a wrapped
# object and propagates method calls to it
# BUT this is more and should be discourage for simple cases

bob = Person("Bob Smith")
sue = Person("Sue Jones", job="dev", pay=100000)
tom = Manager("Tom Jones", 50000)

# Aggregate embedded objects into a composite


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


department = Department(bob, sue)
department.addMember(tom)
department.giveRaise(0.10)
department.showAll()


if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.10)
    print(sue)

    tom = Manager("Tom Jones", 50000)
    tom.giveRaise(0.10)
    print(tom.lastName())
    print(tom)
    print("*" * 50)

    print(list(bob.__dict__.keys()))  # Instance attrs only
    print(dir(bob))  # Instance + inherited attrs in classes
