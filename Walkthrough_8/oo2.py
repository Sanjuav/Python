"""
Class template by JOR
Revision History
06OCT22: Alpha
"""

class_object_attribute1 = 6378137
class_object_attribute2 = 6356752


class MyTemplate():
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        self.attr1 = attribute1
        self.attr2 = attribute2


# Instantiate the class
my_object = MyTemplate("John", True)
# Check the object and type
print(type(my_object))

# Check the object
print(my_object.attr1, my_object.attr2)
