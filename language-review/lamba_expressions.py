""" What are lambda expressions and lambda functions? And how are lambda functions different from other functions in Python?
    - a "lambda expression" it defines a "lambda function"
"""

square = lambda n: n ** 2

print(type(square))  # will point to a function!

print(square(3))


def square_def(n):
    return n ** 2


# Python's built-in sorted function will sort iterable items in ascending order (using the < operator):
fruits = ['lemon', 'apple', 'lime', 'pear', 'watermelon', 'banana']
print(sorted(fruits))

# What if we wanted items by something other than their value? For example, what if we wanted to sort strings by their lengths?
# The sorted function accepts an optional key argument for this:

print(sorted(fruits, key=len))

# The key argument can be any function (technically any callable will do).
# The sorted function will call that function on each item in the given iterable,
# sorting each item by the result of those function calls.

counts = {"apple": 3, "pear": 2, "banana": 4, "lime": 1}
print(counts.items())


# We could define a function that accepts each item and returns the value of that item:

def by_value(item):
    """Return the value from a given (key, value) tuple."""
    key, value = item
    return value


# Then we can pass that function to sorted:

print(sorted(counts.items(), key=by_value))

# Instead of using def to define our function, we could have used a lambda function:

print(sorted(counts.items(), key=lambda item: item[1]))

# It('s up to you when and where you use lambda expressions, '
# but keep in mind that lambda expressions are just a special syntax for
# making a function that doesn(')t have a name. Anything you can do with a lambda function, '
# 'you can do with a non-lambda function.)

