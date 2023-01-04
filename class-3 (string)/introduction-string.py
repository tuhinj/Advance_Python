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
