# function that accepts function

def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

first_last = get_full_name(
    "Binayak",
    "Niraula",
    lambda first_name, last_name:f"{first_name} {last_name}"
)

last_first = get_full_name(
    "Binayak",
    "Niraula",
    lambda first_name, last_name:f"{last_name}, {first_name}"
)

# print(first_last)
# print(last_first)


# function that returns function

def times():
    return lambda x: x*2

double = times()
print(double(2))