# Class 1:
print("Hello World!")

# Class 2: (Introduction to python data types,Operators, Operator precedence, Variables, Comments
'''Text data type: str'''
string = 'Hello World'
print(string)
print(type(string))

'''Numeric Types:	int, float, complex'''
Integers = 12
print(Integers)
print(type(Integers))

floating = 12.3
print(floating)
print(type(floating))

complex_n = 23j
print(complex_n)
print(type(complex_n))

'''Sequence Types:	list, tuple, range'''
List = ["Joy", 23, "Student", "BSC"]
print(List)
print(type(List))

Tuple = ("Joy", 23, "Student", "BSC")
print(Tuple)
print(type(Tuple))

Range = range(23)
print(Range)
print(type(Range))

'''Mapping Type:	dict'''
Dic = {"Name":"Joy", "Age":23, "Job":"Student", "Study":"BSC"}
print(Dic)
print(type(Dic))

'''Set Types:	set, frozenset'''
Set_type = {"Joy", 23, "Student", "BSC"}
print(Set_type)
print(type(Set_type))

Frozenset = frozenset({"Joy", 23, "Student", "BSC"})
print(Frozenset)
print(type(Frozenset))

'''Boolean Type:	boolean'''
a = True
b = False
print(a,b)
print(type(a))
print(type(b))

'''Binary Types:	bytes, bytearray, memoryview'''
Bytes = b"Hello"
print(Bytes)
print(type(Bytes))

Bytearray = bytearray(5)
print(Bytearray)
print(type(Bytearray))

MemoryView = memoryview(bytes(5))
print(MemoryView)
print(type(MemoryView))

'''Variables'''
'''Legal variable names:'''
myvar = "Joy"
my_var = "Joy"
_my_var = "Joy"
myVar = "Joy"
MYVAR = "Joy"
myvar2 = "Joy"

'''Illegal variable names:'''
    #2myvar = "John"
    #my-var = "John"
    #my var = "John"

"""Three type of Variable Names"""
'''Camel Case'''
myVarName = "joy"

'''Pascal Case'''
MyVarName = "joy"

'''Snake Case'''
my_var_name = "joy"

'''Many Values to Multiple Variables'''
a, b, c = "Maynuddin", "Tuhin", "Joy"
print(a,b,c)

'''One Value to Multiple Variables'''
a = b = c = "Joy"
print(a,b,c)

'''Unpack a Collection'''
List = ["Joy", 23, "Student", "BSC"]
a, b, c, d = List
print(a,b,c,d)

'''Concatenation'''
a = "Maynuddin"
b = "Tuhin"
c = "Joy"
print(a + b + c)

'''Comments'''
"""if you use hash in any line of text or sentence make this a comment"""
    # Examples:
    # 12
    # "Hello World"
    # num = 123
    # name = "Joy"
    # Sentence = "My name is Maynuddin Tuhin Joy"

'''Python Casting'''
'''Integers:'''
x = int(1.4)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

'''Floats:'''
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

'''Strings:'''
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# Class 3: (strings Slicing and formatting,string methods, Booleans)
'''strings Slicing'''
slic = "Hello World"
print(slic[0])
print(slic[-1])
print(slic[:5])
print(slic[6:])
print(slic[-11])
print(slic[-11:])
print(slic[-11:-6])
print(slic[-5:])

'''string formatting'''
age = 23
name = "Maynuddin"
txt = "My name is {}, I'm {} years old"
print(txt.format(name, age))
print(f"My name is {name}, I'm {age} years old")

'''string methods'''
    # ---Method--------------Description:
    # ===================================
    # capitalize()-> Converts the first character to upper case

    # casefold()-> Converts string into lower case

    # center()-> Returns a centered string

    # count()-> Returns the number of times a specified value occurs in a string

    # encode()-> Returns an encoded version of the string

    # endswith()-> Returns true if the string ends with the specified value

    # expandtabs()-> Sets the tab size of the string

    # find()-> Searches the string for a specified value and returns the position of where it was found

    # format()->Formats specified values in a string

    # format_map()-> Formats specified values in a string

    # index()	Searches the string for a specified value and returns the position of where it was found

    # join()	Joins the elements of an iterable to the end of the string

    # ljust()	Returns a left justified version of the string

    # lower()	Converts a string into lower case

    # lstrip()	Returns a left trim version of the string

    # maketrans()	Returns a translation table to be used in translations

    # partition()	Returns a tuple where the string is parted into three parts

    # replace()	Returns a string where a specified value is replaced with a specified value

    # rfind()	Searches the string for a specified value and returns the last position of where it was found

    # rindex()	Searches the string for a specified value and returns the last position of where it was found

    # rjust()	Returns a right justified version of the string

    # rpartition()	Returns a tuple where the string is parted into three parts

    # rsplit()	Splits the string at the specified separator, and returns a list

    # rstrip()	Returns a right trim version of the string

    # split()	Splits the string at the specified separator, and returns a list

    # splitlines()	Splits the string at line breaks and returns a list

    # startswith()	Returns true if the string starts with the specified value

    # strip()	Returns a trimmed version of the string

    # swapcase()	Swaps cases, lower case becomes upper case and vice versa

    # title()	Converts the first character of each word to upper case

    # translate()	Returns a translated string

    # upper()	Converts a string into upper case

    # zfill()	Fills the string with a specified number of 0 values at the beginning

m = "hello world, Hello world"
print(m.capitalize())
m1 = "HELLO WORLD"
print(m1.casefold())
print(m1.lower())
print(m.center(50))
print(m.count("world"))
print(m1.encode())
print(m.endswith("hello"))
print(m.find("w"))
print(m.index("H"))
joint = "."
print(joint.join(m1))
print(m1.replace("WORLD", "BANGLADESH"))
print(m1.split())
print(m1.startswith("HELLO"))
print(m.strip())
print(m1.swapcase())
print(m1.title())
print(m.upper())

'''Python - Escape Characters'''

    # Code	Result	
    # \' -> Single Quote	
    # \\ -> Backslash	
    # \n -> New Line	
    # \r -> Carriage Return	
    # \t -> Tab	
    # \b -> Backspace	
    # \f -> Form Feed	
    # \ooo -> Octal value	
    # \xhh -> Hex value
print('Hello \'there\', How are you all? \\ \nI\'m also fine. I think all you know \t What about  \bI\'ll told today.')

'''String Boolean'''
# isalnum()	Returns True if all characters in the string are alphanumeric

    # isalpha()	Returns True if all characters in the string are in the alphabet

    # isdecimal()	Returns True if all characters in the string are decimals

    # isdigit()	Returns True if all characters in the string are digits

    # isidentifier()	Returns True if the string is an identifier

    # islower()	Returns True if all characters in the string are lower case

    # isnumeric()	Returns True if all characters in the string are numeric

    # isprintable()	Returns True if all characters in the string are printable

    # isspace()	Returns True if all characters in the string are whitespaces

    # istitle()	Returns True if the string follows the rules of a title

    # isupper()	Returns True if all characters in the string are upper case
a = 'Hello world, It\'s my first code here in python, I\'m 23 years old'
print(a.isalnum())
print(a.isalpha())
print(a.isdecimal())
print(a.isdigit())
print(a.islower())
print(a.istitle())
print(a.isspace())
print(a.istitle())
print(a.isupper())

'''The following will return False:'''
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Class 4: (conditional logic: if, else and elif, comparison operator and logical, operator in details, Nesting conditions, Short hand if - else (ternary))
'''Python divides the operators in the following groups:
> Arithmetic operators (+,-,*,/,%,**,//)
> Assignment operators (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)
> Comparison operators (==, !=, >, <, >=, <=)
> Logical operators (and, or, not)
> Identity operators (is, is not)
> Membership operators (in, not in)
> Bitwise operators (&: AND, |: OR, ^: XOR, ~: NOT, <<: Zero fill left shift, >>: Signed right shift)
'''
a = 12
b = 5
print(a+b,a-b,a*b,a/b,a%b,a**b,a//b)
a+=b
print(a)
a%=b
print(a)
a**=b
print(a)
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)
print(a==b and b==a)
print(a!=b or b!=a)
print(a is 23, b is not 6)
l = [1, 3, 4, 6, 9]
print(5 in l, 10 not in l)

'''conditional logic: if, else and elif'''
x = 4
y = 43
if x != y:
    print("It's correct!")

if x == y:
    print("It's Correct!")
elif x > y:
    print("It's Correct!")
else:
    print("It's not Correct!")

    '''Short Hand If'''
if x == y: print("It's correct!")
print("It's Correct!")if x > y else print("It's not Correct!")

'''Nested If'''
if x < 6 and y < 5:
    print("Condition True")
    if x != y:
        print("Condition True!")
    else:
        print("Condition False")
else:
    print("...!!!!It's Wrong!!!!...")

# Class 5: (While loop, For loop, Nesting loops, Break, continue and else in loops)
'''For loop'''
List = ["Joy", 23, "Student", "BSC"]
# for l in List:
#     print(l)

for al in "MAYNUDDIN":
    print(al)

    '''The break Statement'''
for a in List:
    print(a)
    if "Maynuddin" not in List:
        print("Rejected!")
        break
    else:
        ("Accpted!")
        
    '''The continue Statement'''
for a in List:
    print(a)
    if "Maynuddin" in List:
        print("Accpted!")
        continue
    else:
        ("Not Accpted!")
    '''The range() Function'''
for x in range(6):
  print(x)

for x in range(10, 50, 5):
  print(x)

  '''Nested Loops'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

    '''Else in For loop'''
for x in range(100):
  print(x)
else:
  print("Finally finished!")

"""While Loop"""
i = 0
while i <= 6:
    print(i)
    i+=2

    '''The break Statement'''
i = 1
while i < 11:
    print(i)
    if i == 6:
        print("Oh! got it!!!")
        break
    i += 2

    '''The continue Statement'''
i = 2
while i < 11:
    i += 2
    if i > 6:
        continue
    print(i)

    '''The else Statement'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Class 6: (list in Python, List methods, List comprehension, Introduction to tuple in Python, Tuple methods, Tuple unpacking)
"""LIST"""
List = ['Joy', 23, 'Student', 'BSC', 'CSE', True]
print(List)
print(len(List))
print(type(List))

'''make list'''
List2 = list(('Joy', 23, 'Student', 'BSC', 'CSE', True))
print(List2)
print(type(List2))

'''Access items'''
List2 = ['Joy', 23, 'Student', 'BSC', 'CSE', True]
print(List2[1])
print(List2[-1])
print(List2[:3])

'''Check if Item Exists'''
L1 = ["Apple","Banana","Orange"]
if "Banana" in L1:
    print("Apple in List")

'''Change Item Value'''
L2 = ["Apple","Banana","Orange"]
L2[1] = "Mango"
print(L2)

L2[:2] = ["Lichi","Date", "Jackfruit"]
print(L2)

L3 = ['Lichi', 'Date', 'Jackfruit', 'Orange']
L3.insert(2, "Apple") # add item by 'insert' use index and item name
print(L3)

L1.append("Lichi") # add item by 'append'
print(L1)

L1.extend(L2) # add two list by 'extend'
print(L1)

L1.remove("Apple") # delete item by "remove"
print(L1)

L1.pop() # delete item by "pop"
print(L1)

L1.pop(1)
print(L1)

del L2  # delete list by using "del"
# print(L2)

L3.clear() # empty list by "clear"
print(L3)

L1.sort() # arrange list by "sort"
print(L1)

L1.reverse() # reverse list by "reverse"
print(L1)

'''Loop Lists'''
List = ['Lichi', 'Date', 'Jackfruit', 'Orange']
for x in List:
    print(x)

'''Loop Through the Index Numbers'''
List1 = ['Lichi', 'Date', 'Jackfruit', 'Orange']
for a in range(len(List1)):
    print(a,List[a])

'''Using a While Loop in List'''
Lis = ['Apple','Lichi', 'Date', 'Jackfruit', 'Orange']
i = 0
while i < len(Lis):
    print(i, Lis[i])
    i += 1

'''List Comprehension'''
m = ['Date', 'Jackfruit', 'Orange']
[print(x) for x in m]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

print(Lis + List2) # concatenate two list by "+"

"""TUPLE"""
t1 =("apple", "banana", "cherry", "kiwi", "mango")

print(len(t1)) # show length by "len"

print(type(t1))

'''Access Tuple Items'''
t1 =("apple", "banana", "cherry", "kiwi", "mango")
print(t1[3])

if 'banana' in t1:
    print("Cool!....")

'''Python - Update Tuples'''
t1 =("apple", "banana", "cherry", "kiwi", "mango")
t2 = list(t1)
t2[2] = "orange"
t1 = tuple(t2)
print(t1)

t1 =("apple", "banana", "cherry", "kiwi", "mango")
t2 = list(t1)
t2.append("orange")
t1 = tuple(t2)
print(t1)

t1 =("apple", "banana", "cherry", "kiwi", "mango")
t2 = list(t1)
t2.remove("mango")
t1 = tuple(t2)
print(t1)

t1 =("apple", "banana", "cherry", "kiwi", "mango")
t2 = list(t1)
t2.clear()
t1 = tuple(t2)
print(t1)

t1 =("apple", "banana", "cherry", "kiwi", "mango")
del t1
# print(t1)

'''Unpack Tuples'''
t1 =("apple", "banana", "cherry", "kiwi", "mango")
f1,f2,f3,f4,f5=t1
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)

t1 =("apple", "banana", "cherry", "kiwi", "mango")
f1,f2,*f3=t1
print(f1)
print(f2)
print(f3)

'''Loop Tuple'''
Tuple = ('Lichi', 'Date', 'Jackfruit', 'Orange')
for x in Tuple:
    print(x)

'''Loop Through the Index Numbers'''
Tuple1 = ('Lichi', 'Date', 'Jackfruit', 'Orange')
for a in range(len(Tuple1)):
    print(a,Tuple1[a])

'''Using a While Loop in List'''
Lis = ('Apple','Lichi', 'Date', 'Jackfruit', 'Orange')
i = 0
while i < len(Lis):
    print(i, Lis[i])
    i += 1

'''List Comprehension'''
m = ('Date', 'Jackfruit', 'Orange')
(print(x) for x in m)

fruits = ("apple", "banana", "cherry", "kiwi", "mango")
newlist = ()

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

fruits = ("apple", "banana", "cherry", "kiwi", "mango")

newlist = (x for x in fruits if "a" in x)

print(newlist)

print(Tuple1 + Tuple) # concatenate two list by "+"

# Class 7: (Accessing and looping set items, Set methods, Accessing and looping dictionary items, Dictionary methods)
"""SET"""
Set = {"apple", True, 234, "Tuhin"}
print(type(Set))

print(len(Set))

'''Access Set Items'''
Set1 = {"apple", False, 12, "Joy"}
for a in Set1:
    print(a)

print("Tuhin" in Set1)

Set.add("Joy") # add item by "add"
print(Set)

Set.update(Set1) # add two set by "upbate"
print(Set)

Set.remove("Tuhin") # delete item by "remove"
print(Set)

Set.discard("Joy") # remove savely by "discard"
print(Set)

Set.pop() # remove last item by "pop"
print(Set) 

Set.clear() # clear set by "clear"
print(Set)

del Set1
# print(Set1)

Set3 = {"apple", True, 234, "Tuhin"}
for a in Set3:
    print(a)

'''Join Sets'''
s1 = {1,2,3,4}
s2 = {1,4,6,9,8}

s3 = s1.union(s2) # joined two set in a variable by "union"
print(s3)

s1.update(s2) # joined two set by "update"
print(s1)

s1 = {1,2,3,4}
s2 = {1,4,6,9,8}

s = s1.intersection(s2) # two set in a variable but only common value by "intersection"
print(s)

s1.intersection_update(s2) # joined two set but only common value output by "intersection_update"
print(s1)

s1 = {1,2,3,4}
s2 = {1,4,6,9,8}

s = s1.symmetric_difference(s2) # two set in a variable but only uncommon value by "symmetric_difference"
print(s)

s1.symmetric_difference_update(s2) # joined two set but only uncommon value output by "symmetric_difference_update"
print(s1)

"""DICTIONARIES"""
Dic = {"Name":"Joy", "Age":23, "Job":"Student", "Study":"BSC"}
print(type(Dic))

nDis = dict(Name="Joy", Age=23, Job="Student", Study="BSC")
print(nDis)

print(nDis["Name"])

'''Accessing Items'''
Dic = {"Name":"Joy", "Age":23, "Job":"Student", "Study":"BSC"}
print(Dic["Age"])

x = Dic.get("Job")
print(x)

print(Dic.keys())

print(Dic.values())

a = Dic.items()
print(a)

if "Name" in Dic:
    print("Yes!!!!")

'''Add & Change Dictionary Items'''
Dic["Name"] = "Maynuddin Tuhin Joy"
print(Dic)

Dic.update({"Blood_G": "B+"})
print(Dic)

Dic.pop("Job")
print(Dic)

Dic.popitem()
print(Dic)

Dic.clear()
print(Dic)

del Dic
# print(Dic)

'''Loop Dictionaries'''
Dic = {"Name":"Joy", "Age":23, "Job":"Student", "Study":"BSC"}
for a in Dic:
    print(a)

for b in Dic.items():
    print(b)

for c in Dic.values():
    print(c)

for d in Dic.keys():
    print(d)

for x, y in Dic.items():
    print(x,y)

'''Copy Dictionary'''
Dic = {"Name":"Joy", "Age":23, "Job":"Student", "Study":"BSC"}
Dic2 = Dic.copy()
print(Dic2)

Dic3 = dict(Dic)
print(Dic3)

'''Nested Dictionaries'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily1 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily1)

# Class 8: (Getting started with function in Python, Recursive function, Introduction to lambda function in Python, Introduction to built in function in Python, Scopes in Python, Pass statement in python)
"""Python Functions"""
def my_function():
    print("Hello World")
my_function()

def full_name(firstn): # Arguments
    print(firstn + " Joy")
full_name("Maynuddin")
full_name("Tuhin")

def my_name(firstn, lastn):
    print(firstn,lastn)
my_name("Maynuddin","Tuhin Joy")

def fruit(*name): # Make a tuple by this Arguments '*name'
    print(name)
fruit("Jackfruit","Lichi","Mango", "Banana")

def family_member(**name): # Make a Dictionary by this Arguments '**name'
    print("My family member:",name)
family_member(Father = "Jamal",Mother = "Jesmin", Son = "Kabir")

'''Default Parameter Value'''
def your_name(name = "Please enter your name"):
    print("My name is " + name)
your_name()
your_name("Joy")

def fruits_name(fruit): # Passing a List as an Argument
    for x in fruit:
        print(x)
fruite_list = ["Banana", "Apple", "Jackfruit"]
fruits_name(fruite_list)

def math(a):
    return 2 * a
print("Result:",math(5))
print("Result:",math(10))

def myfunction(): # put in the pass statement to avoid getting an error.
  pass

"""Recursive function"""
def rec_fun(k):
    if (k > 0):
        result = k + rec_fun(k - 1)
        print(result)
    else:
        result = 0
    return result
rec_fun(10)

"""LAMBDA"""
x = lambda a : a + 12
print("Sum:",x(2))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(10))

def myfunc(a):
    return lambda x : x * a
myfun_num = myfunc(2)
myfun_num1 = myfunc(4)

print("LAMBDA",myfun_num(12))
print("LAMBDA",myfun_num1(10))

"""Scopes"""
def fun_1():
    x = 300
    print(x)
fun_1()

def f_1():
    x = 1000
    def f_2():
        print(x)
    f_2()
f_1()

'''Global variables'''
x1 = 400
def func_1():
    print(x1)
func_1()

x2 = 700
def func_2(num1):
    global x2
    a = x2 + num1
    print("sum:",a)
func_2(300)

'''Pass'''
def function1(word):
    pass

# Class 9: (basic modules, Built in modules in Python, Working with Python Dates, Working with Math module, Introduction to PIP)
"""Modules"""
'''Creating a module.py file and inport it by using "import" '''
# def full_name(firstn):
#     print(firstn + " Joy")

import modul
modul.full_name("Maynuddin Tuhin Joy")

print(modul.family["Father"], modul.family["Mother"], modul.family["Name"])

'''Re-naming a Module'''
import modul as joy
joy.full_name("Hasibul Islam Shanto")

import platform
print(platform.system())
print(platform.architecture())
print(platform.freedesktop_os_release())
print(platform.node())
print(platform.machine())
print(platform.python_compiler())
print(platform.uname())
print(dir(platform))

'''Datetime'''
import datetime
print(datetime.datetime.now())
a = datetime.datetime.now()
print(a.year)
print(a.strftime("%A"))
print(datetime.datetime(1999, 7, 6))

'''Math'''
'build-in math functions'
a = min(4, 2, 5, -4, -1)
b = max(4, 2, 5, -4, -1)
print("Max number:",b,"\nMin number:", a)

c = abs(-4.55654) 
print("Absolute(positive) value:",c)

d = pow(5, 2)
print("The value of 5 to the power of 2:", d)

'''The Math Module'''
import math
x = math.sqrt(49)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

z = math.pi
print(z)

