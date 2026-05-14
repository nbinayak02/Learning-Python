# Swap two variables without a third variable

a = 10
b = 20

print(f"a is {a} and b is {b}")

a = a + b
b = a - b
a = a - b

print(f"a is {a} and b is {b}")

a, b = b, a # one liner, python way!
