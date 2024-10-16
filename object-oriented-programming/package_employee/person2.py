class AttrDisplay:
    """
    Provides an inheritable print overload method that displays instances
    with their class names and a name=value pair for each attribute stored
    on the instance itself (but not attrs inherited from its classes). Can
    be mixed into any class, and will work on any instance.
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append("%s=%s" % (key, getattr(self, key)))
        return ", ".join(attrs)

    def __str__(self):
        return "[%s: %s]" % (self.__class__.__name__, self.gatherAttrs())


class Person(AttrDisplay):
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


class SuperClass:
    def __init__(self, x):
        pass


class Sub(SuperClass):
    def __init__(self, x, y):
        Super.__init__(self, x)
        pass


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
