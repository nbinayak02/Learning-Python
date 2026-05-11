# Program to find even/odd, positive/negative and prime

n = input("Enter a number: ")
number = int(n)
factors = []


if(number % 2 == 0):
    print(number," is even number.")
else:
    print(number, " is odd number.")

if(number < 0):
    print(number, " is negative number.")
else:
    print(number, " is positive number.")
    
    for i in range(1, number+1):
    
        print("The value of i is ",i)
    
        if(number % i == 0):
            factors.append(i)
            print("Factors: ",factors)

    if( number == 1):
        print(number, " is prime number.")
    elif(factors == [1, number]):
        print(number, " is prime number.")
    else:
        print(number, " is composite number.")
        