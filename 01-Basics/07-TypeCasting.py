# implicit type casting
a = 200
b = 34.67
c = a+b
print(c,type(c))

d = True #boolean will converted into int first
e = d+b 
print(e, type(e)) 

# Explicit type casting
print(int(b),type(int(b))) # float to int
print(int(d), type(int(d))) #boolean to int
print(int("100"), type(int("100"))) #string to int
print(int("10"+"02"), type(int("10"+"02")))
print(int("101100101",2)) # binary to int
print(int("234",8)) #octal to int
print(int("345af",16))#hex to int

print(float(2045)) #int to float!
print(float("234.98"))#string to float
print(float("10E-4"))#scientific notation to float

print(str(10), type(str(10)))#int to str
print(str(3.345e4))#float to str

#conversion of sequence type