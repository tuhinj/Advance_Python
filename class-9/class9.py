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