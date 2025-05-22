"""
Source: https://realpython.com/ref/builtin-functions/classmethod/
https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
The most common use cases for the @classmethod include:
    Creating multiple constructors for flexibility in instantiation.
    Implementing factory methods to encapsulate complex object creation logic.
    Modifying class-level attributes that apply to all instances.
"""


"""
As an alternative constructor:
"""
class ThreeDPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

    def __repr__(self):
        return f"ThreeDPoint(x={self.x}, y={self.y}, z={self.z})"

# Usage
print(
    ThreeDPoint.from_sequence((4, 8, 16))
)  # Output: ThreeDPoint(x=4, y=8, z=16)


"""
A common real-world application of @classmethod is to create factory methods that return 
pre-configured instances of a class. For example, a Pizza class might have class methods 
for creating specific types of pizza:
"""
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])

    def __str__(self):
        return f"Pizza with {' and '.join(self.ingredients)}"

# Usage
print(
    Pizza.margherita()
)  # Output: Pizza with mozzarella and tomatoes
print(
    Pizza.prosciutto()
)  # Output: Pizza with mozzarella and tomatoes and ham
