# Function
'''Creating a Function & Calling a Function'''

def print_function():
    print("Hello World!")
print_function()

'''Arguments'''
def print_argument(fname, lname):
    print(fname,lname)

print_argument("Maynuddin","Tuhin")
# print_argument("Tuhin") # Dosen't work "TypeError"


'''Arbitrary Arguments, *args'''
def print_tuple(*name):
    print(name)
print_tuple("Maynuddin", "Tuhin", "Joy", "Pronoy", "Shanto")

'''Keyword Arguments'''
def print_keywords(name, age, cls):
    print(f"My name is {name}, I'm {age} years old and I am student of {cls}")

print_keywords(name="Maynuddin Tuhin Joy", age= 23, cls = "BSC")

'''Arbitrary Keyword Arguments, **kwargs'''
def dic_args(**key_value):
    print(key_value)

print(Name= "Maynuddin Tuhin Joy", age = 23, hight = 5.4)

