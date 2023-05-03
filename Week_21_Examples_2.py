from readline import set_history_length


print('--- Classes ---')
# defining classes in Python is similar to most OOP languages

# when you instantiate a class, you get an object

# an object is an instance of a class -- it's actually called object

# this is how you define a class -- USE A CAPITAL LETTER
# for multiple words us CapitalCase


class Dog():
    # these are class VARIABLES
    total_dogs = 0
    LIKES_PETS = True  # all dogs like pets -- all caps is a convention for constants in Python
    # the __init__ method in Python is analogous to constructor() in JS

    def __init__(self, name, age=0):  # age is a default parameter
        # self will be a param for all class methods
        # it is analogous to "this" in JS
        # it refers to this particular instance of this class
        # defining an ATTRIBUTE on this instance called identity #(analogous to property in JS)
        self.identity = "dog"
        self.name = name  # you can set attribute based on the param in __init__
        self.age = age
        # the variables above are INSTANCE attributes/variables
        # they are specific to the instance
        # you can also define CLASS VARIABLES
        Dog.total_dogs += 1  # (same as Dogs.total_dogs = Dogs.total_dogs + 1)
        print("Dog number {} was just born!!!".format(Dog.total_dogs))

    # class method --- don't forget (self)
    def bark_hello(self):
        print("Woof I am {}".format(self.name))
        print(f"I said BARKBARK I am {self.name}")

    # class method --- don't forget (self)
    def describe(self, someone):
        print(
            f"Hello {someone}, I am {self.name}, a {self.age} year old {self.identity} BWOOOOOOOOARrWWWAR 🐕‍🦺")


# this is how you instantiate in Python
puppy = Dog("MJ")  # using the default param value

print("\nhere's what we got when we instantiated Dog")
print(puppy)

# you can access attributes with dot
print("here is the puppy.identity")
print(puppy.identity)
print("here is puppy.name")
print(puppy.name)

my_best_friend = Dog("Luna")

# ex: write a method that takes an arg and prints a string with borth the parameter and a class attribute of your choice interpolate into it
# test it by calling
my_best_friend.describe("Deja")

fluffy_boy = Dog("Floofer", 7)  # overriding the default param value
fluffy_boy.describe('Gore')

# accessing class variable
print(f"There are {Dog.total_dogs} dogs so far.")
print("Dogs like pets, true or false")
print(Dog.LIKES_PETS)

# to print all ATTRIBUTES
# print(puppy.__dict__)

print("\n\n\n---- inheritance: ----\n")

# INHERITANCE


class Parent():

    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = "Wallen"

    def say_hello(self):
        print(f"Hello I am {self.first_name} {self.last_name}")

    def emote(self):
        print("Life is intense. BRING IT ON!!!")

# in Python, to do inheritance, include the name of the parent class in the ()


class Child(Parent):  # analogous to "class Child extends Parent" in JS

    def __init__(self, first_name):
        # in JS we would class super(), in Python you just explicitly call the init method of the parent class
        Parent.__init__(self, first_name)

    # override method from the parent class
    def say_hello(self):
        print(
            f"I am {self.first_name} {self.last_name} AND PARENTS JUST DONT UNDERSTAND :( ")

    # if you must extend a parent class method
    # call that method explixitly on the Parent class and pass in self (just like in __init__)
    # then add whatever additional code you need
    def emote(self):
        Parent.emote(self)  # call emote() in parent on this instance
        print('...but its fun! :)')


hunter = Parent("Hunter")
hunter.say_hello()
hunter.emote()

shiloh = Child("Shiloh")
shiloh.say_hello()
shiloh.emote()

# built in class attribute

# e.g. .__dict__

# to have your objects' attributes and values to print nicely
# you can access the .__dict__ property

# this shows the class the object is an instance of and its location in memory
print(shiloh)

print(shiloh.__dict__)  # this gives you the key value pairs

# There are several others -- google them !!

print("\n\n")

print(type(shiloh) == Child)
print(type(hunter) == Parent)
