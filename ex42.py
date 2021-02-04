## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Make a class named Dog that is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a __init__ that takes self and name parameters
        self.name = name

## Make a class named Cat that is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a __init__ that takes self and name parameters
        self.name = name

## Make a class named Person that is-a object
class Person(object):

    def __init__(self, name):
        ## class Person has-a __init__ that takes self and name parameters
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Make a class named Employee that is-a Person (taking Person class blueprint)
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        # My guess before research is this is basically
        # self.name = name
        super(Employee, self).__init__(name)
        ## Employee has-a attribute salary
        self.salary = salary

## Create a class named Fish that is-a object
class Fish(object):
    pass

## Make a class named Salmon that is-a Fish
class Salmon(Fish):
    pass

## Make a class named Halibut that is-a Fish
class Halibut(Fish):
    pass


## Set rover to an instance of class Dog with the argument(parameter?) "Rover"
rover = Dog("Rover")

## Set satan to an instance of class Cat with the argument(parameter?) "Satan"
satan = Cat("Satan")

## Set mary to an instance of class Person with the argument(parameter?) "Mary"
mary = Person("Mary")

## From mary get the pet attribute and set it to satan
mary.pet = satan

## set frank to an instance of Employee with the argument(parameter?) of name = "Frank" and salary = 120000
frank = Employee("Frank", 120000)

## From frank grab the pet attribute and set it to rover
frank.pet = rover

## Set flipper to an instance of class Fish
flipper = Fish()

## Set crouse to an instance of class Salmon
crouse = Salmon()

## Set harry to an instance of class Halibut
harry = Halibut()
