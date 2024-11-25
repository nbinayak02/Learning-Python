# Integer Interning
a = 100
b = 100

print(a is b) #returns true
# is checks if variable a and b refers to same object. It is true because python stores value once in memory and if other different variable have same value, they are not stored in different location instead they refer to same value


print(id(a), id(b)) #returns 138268271059984 138268271059984
# id() returns the memory location where these values are stored. since a, b store same value i.e. a=b=100, they are not seperately stored. 100 is stored once in memory and a,b refer to same 100


a=a+30
print(a, b) #returns 130 100
print(a is b) #now returns false
print(id(a), id(b)) # returns 135426227446768 135426227446800

# The operation a = a + 30 creates a new object with the value 130. Since integers are immutable, modifying a doesn't change the original 100. Instead, a new integer object 130 is created and assigned to a. b is still referring to the original 100. Now, a is b evaluates to False because a and b point to different objects.  id(a) and id(b) return different memory addresses.


b=b+30
print(a, b) # returns 130 130
print(a is b) #returns true
print(id(a), id(b))

#When b = b + 30: Python creates the value 130 again. However, since 130 is within the cached range (-5 to 256), both a and b point to the same cached object for 130.

# Interning is an optimization technique used by Python to reuse immutable objects (like small integers, strings, etc.) that have the same value to save memory and improve performance. Instead of creating a new object every time a value is needed, Python reuses existing objects under certain conditions. Python preallocates and caches integers in a specific range (typically -5 to 256). Integers in this range are reused, so all variables referring to the same value in this range point to the same memory location. The concept of object interning ensures efficient memory usage and performance by reusing immutable objects under specific conditions. It's the reason why small integers and some strings with the same value share the same memory address in Python.