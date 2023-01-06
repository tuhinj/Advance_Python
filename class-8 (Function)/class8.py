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
