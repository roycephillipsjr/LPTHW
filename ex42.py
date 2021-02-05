## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

    # Trying not to repeat myself so putting things that will be constants on all animals
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def who_am_i(self):
        pass

## Make a class named Dog that is-a Animal
class Dog(Animal):

    animal_type = 'dog'

    def who_am_i(self):
         print(f"Hello my name is {self.name} and I am a dog!")

    def speak():
        print("WOOF!!!")

## Make a class named Cat that is-a Animal
class Cat(Animal):

    animal_type = 'cat'

    def who_am_i(self):
        print(f"Hello my name is {self.name} and I am cat!")

    def speak():
        print("MEOW!!!")

## Make a class named Person that is-a object
class Person(object):

    def __init__(self, name):
        ## class Person has-a __init__ that takes self and name parameters
        self.name = name
        self.age = None
        ## Person has-a pet of some kind
        self.pet = None

    def who_am_i(self):
        print(f"Hello my name is {self.name} and my pet's name is {self.pet.name} and they are a {self.pet.animal_type}!!")



## Make a class named Employee that is-a Person (taking Person class blueprint)
class Employee(Person):

    def __init__(self, name, salary, job_title):
        ## ?? hmm what is this strange magic?
        # My guess before research is this is basically
        # self.name = name
        super(Employee, self).__init__(name)
        ## Employee has-a attribute salary
        self.salary = salary
        self.job_title = job_title



## Create a class named Fish that is-a object
class Fish(object):

    def __init__(self):
        self.age = None
        self.color = None


## Make a class named Salmon that is-a Fish
class Salmon(Fish):

    def __init__(self):
        self

## Make a class named Halibut that is-a Fish
class Halibut(Fish):

    def __init__(self):
        self


## Set rover to an instance of class Dog with the argument(parameter?) "Rover"
rover = Dog("Rover", "Lab", 2)

## Set satan to an instance of class Cat with the argument(parameter?) "Satan"
satan = Cat("Satan", "Tabby", 5)

## Set mary to an instance of class Person with the argument(parameter?) "Mary"
mary = Person("Mary")

## From mary get the pet attribute and set it to satan
mary.pet = satan

## set frank to an instance of Employee with the argument(parameter?) of name = "Frank" and salary = 120000
frank = Employee("Frank", 120000, 'Software Engineer')

## From frank grab the pet attribute and set it to rover
frank.pet = rover

## Set flipper to an instance of class Fish
flipper = Fish()

## Set crouse to an instance of class Salmon
crouse = Salmon()

## Set harry to an instance of class Halibut
harry = Halibut()


rover.who_am_i()
print(mary.name)
print(mary.pet.name)
mary.who_am_i()
