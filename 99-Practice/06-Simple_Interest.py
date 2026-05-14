# Calculate simple interest given principal, rate, and time

principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100

print(f"The interest is {simple_interest}")