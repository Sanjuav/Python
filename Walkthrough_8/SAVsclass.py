"""
Simple Class by JOR, by convention, use camel case to name classes
"""
# Create a class
class SAVsClass():

 # Constructor, called whenever an instance of the class is created.
 def __init__(self, my_greeting):
    print("Running constructor for SAVsClass")
 # Create attributes and set initial values
    self.message = my_greeting
 def my_method(self):
    print(self.message)
my_class2 = SAVsClass("Morning Sanju!")
my_class2.my_method()
print(type(my_class2))