# defining variables
meter = 1000
kilometer = 1.0
name = "KM"

# printing variables
print(meter)
print(kilometer)
print(name)

# deleting variable
del kilometer
# print(kilometer) provides error

sagarmatha = 8848.86

# type of variable
print(type(meter))
print(type(name))
print(type(sagarmatha))

# casting variable
x = str(200)
print(x, type(x)) 

# multiple assignments
a = b = c = 100
print(a,b,c)

x, y, z = "Hello", 48, 456.75
print(x, y, z)

# local variable
def sum(e, f):
    sum = e + f
    return sum
print(sum(34,76))
# print(e) cannot access local variable

# global variable
# all variable declared outside functions are global variables
def add():
    return y + z
print(add())

# constants
PI = 3.14
print(PI)
PI = 34
print(PI)
# Python doesnot have official constant mechanism. However constant is denoted by defining variable name is uppercase




