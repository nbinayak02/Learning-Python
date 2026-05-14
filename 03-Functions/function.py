def greet():
    print("Hello!")

# greet()

def count_to_zero(number):
    print(number);
    if(number != 0):
        count_to_zero(number-1)

count_to_zero(3)
        