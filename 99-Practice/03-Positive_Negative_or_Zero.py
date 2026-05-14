# Check if a number is positive, negative, or zero

input_num= input("Enter a number: ")
input_num = int(input_num)

if(input_num == 0):
    print("The number is zero")
elif (input_num > 0):
    print("The number is positive.")
else:
    print("The number is negative.")