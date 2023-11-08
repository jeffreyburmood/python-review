""" this script will explore how the eval() function works """

tupleString = '(1,2)'
print(type(tupleString))
tuple = eval(tupleString) # this will essentially convert the string entity into an entity of the base type - tuple
print(type(tuple))
print(f'tuple values = {tuple[0]}, {tuple[1]}')

numberString = '1'
print(type(numberString))
number = eval(numberString) # this will essentially convert the string entity into an entity of the base type - number
print(type(number))
print(f'number value = {number}')
