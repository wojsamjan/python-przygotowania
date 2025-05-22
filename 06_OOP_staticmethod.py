"""
Source: https://realpython.com/ref/builtin-functions/staticmethod/
https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
The most common use cases for the staticmethod() function include:
    Grouping utility functions within a class
    Providing a function that doesn’t need access to class or instance data
    Creating a namespace for related functions
"""


"""
Consider a Formatter class that provides methods to format numbers as currency and 
percentages. These methods don’t rely on instance or class data, so they can be defined as 
static methods:
"""
class Formatter:
    @staticmethod
    def as_currency(value):
        return f"${value:,.2f}"

    @staticmethod
    def as_percent(value):
        return f"{value:.2%}"

# Usage
formatter = Formatter()
print(formatter.as_currency(1000))  # Output: $1,000.00
print(formatter.as_percent(0.25))  # Output: 25.00%

"""
In this example, .as_currency() and .as_percent() are static methods that format 
numbers without needing access to any instance or class variables. This helps in 
logically grouping utility functions within the Formatter class.
"""
