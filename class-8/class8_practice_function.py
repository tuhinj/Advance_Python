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
# print("Joy's age is:",joy_age)

tuhin = 12
def passing_years(yrs):
    return tuhin + yrs
# print("Tuhin's age is:",passing_years(10))

'''Parameters'''
def print_name(fast_name, last_name):
    print("Print your name:"+fast_name +" "+ last_name)

print_name("Tuhin","Joy")

'''Arbitarary Arguments'''
def print_list(*name):
    print("It's Tuple:",name)
    print("It's List:",list(name))

print_list("tuhin", "joy", "maynuddin")

'''Default Parameter Value'''
def full_name(firstn, lastn = "Joy"):
    print(firstn, lastn)

full_name("Maynuddin","Tuhin")
full_name("Tuhin",)

'''Passing a List as an Argument'''
def new_function(foods):
    for food in foods:
        print(food)
food_list = ["Apple","Brade","Tea","Coffe","Rice"]
new_function(food_list)

'''Return Values'''
def new_input(age):
    return 23 + age
print(new_input(10))

'''pass function'''
def value(n):
    pass
print(value(34))