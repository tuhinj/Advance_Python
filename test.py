# Class 1:
print("Hello World!")

# Class 2: (Introduction to python data types,Operators, Operator precedence, Variables, Comments
'''Text data type: str'''
string = 'Hello World'
print(string)
print(type(string))

'''Numeric Types:	int, float, complex'''
intger = 12
print(intger)
print(type(intger))

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

'''concatenation'''
a = "Maynuddin"
b = "Tuhin"
c = "Joy"
print(a + b + c)

