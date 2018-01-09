# CLASSES

# Creating a class


class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        # self is a reference to the instance
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is sitting.")

    def roll_over(self):
        """Simulate a dog rolling over"""
        print(self.name.title() + " rolled over!")

my_dog = Dog("Buddy", 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

# Ex. 5 Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant
#_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and
# a method called open_restaurant() that prints a message indicating that the restaurant is open. Then, make an
# instance called restaurant from your class. Print the two attributes individually, and then call both methods.

# Inheritance


class Husky(Dog):
    """Creating a type of dog with similar attributes"""
    def __init__(self, name, age):
        """Initialize attributes of the parent class."""
        super().__init__(name, age)
        self.eye_color = 'jade'

    def describe_husky(self):
        """Talk about the husky."""
        print("This is my beautiful husky named " + self.name.title() + " who is " + str(self.age) +
              " years old and has " + self.eye_color + " eyes.")

my_husky = Husky('Alaskan princess', 2)
my_husky.describe_husky()
my_husky.eye_color = 'aqua'
my_husky.describe_husky()
