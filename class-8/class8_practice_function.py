# function

def print_hello():
    print("hello")

# print_hello()

def print_hello(neme):
    print(f"Hello {neme}")

# print_hello("joy")

# def print_name(name):
#     input_name = input()
#     print("Hi",input_name,name)

# print_name("joy")

joy_age = 12
def passing_years(years):
    global joy_age
    joy_age += years
    # print(joy_age)
passing_years(10)
print(joy_age)
