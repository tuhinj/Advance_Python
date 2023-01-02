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
'''While loop'''