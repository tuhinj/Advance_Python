# Class 2: (Introduction to python data types,Operators, Operator precedence, Variables, Comments
'''Text data type: str'''
string = 'Hello World'
print(string)
print(type(string))
s="Hey Python myself Maynuddin Tuhin Joy"
print(string, type(s))

'''Numeric Types:	int, float, complex'''
Integers = 12
print(Integers)
print(type(Integers))
i=12
print(i, type(i))

floating = 12.3
print(floating)
print(type(floating))
f=12.1
print(f, type(f))

complex_n = 23j
print(complex_n)
print(type(complex_n))
c=12j
print(c, type(c))

'''Sequence Types:	list, tuple, range'''
List = ["Joy", 23, "Student", "BSC"]
print(List)
print(type(List))
l=["tuhin", 12, 12.1, 'student']
print(l, type(l))

Tuple = ("Joy", 23, "Student", "BSC")
print(Tuple)
print(type(Tuple))
t=('Maynuddin', 21, 3.23, "BCS")
print(t, type(t))

Range = range(23)
print(Range)
print(type(Range))
r=range(12)
print(r,type(r))


'''Mapping Type:	dict'''
Dic = {"Name":"Joy", "Age":23, "Job":"Student", "Study":"BSC"}
print(Dic)
print(type(Dic))
d={"name":"007","age":23, "job":"Student"}
print(d,type(d))

'''Set Types:	set, frozenset'''
Set_type = {"Joy", 23, "Student", "BSC"}
print(Set_type)
print(type(Set_type))
s={"007","Jemse Bond"}
print(s, type(s))

Frozenset = frozenset({"Joy", 23, "Student", "BSC"})
print(Frozenset)
print(type(Frozenset))
f=frozenset('joy',34,"student")
print(f, type(f))


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
