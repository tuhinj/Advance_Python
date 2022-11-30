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

dic_args(Name = "Maynuddin Tuhin Joy", age = 23, hight = 5.4)

'''Default Parameter Value'''
def default_value_set(fname,lname = "Joy"):
    print("My Name is:", fname,lname)
default_value_set("Maynuddin","Tuhin")
default_value_set("Tuhin")

'''Passing a List as an Argument'''
joy = {"Maynuddin", "Tuhin", "Joy", "Pronoy", "Shanto"}

def  list_passing(names):
    print(names)
    for name in names:
        print(name)

list_passing(joy)

'''Return Values'''
def return_value(year):
    if year % 4 == 0 or (year % 400 and year % 100 != 0):
        print("leap year")
    else:
        print("not leap year")

return_value(1197)

def num_multiapply(num):
    return 3 + num
print(num_multiapply(34))

'''The pass Statement'''
def pass_function(num):
    pass
    # print("Hello World",num)
    
pass_function(32)

'''Recursion'''
list1 = [1, 2, 3, 4, 5]
def print_list (num):
    if num == len(num):
        num.pop()
    return num
print_list(list1)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(15)