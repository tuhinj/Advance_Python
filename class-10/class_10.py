# def calculate_balance(cash_in_bank, cash_in_hand):
#     if cash_in_hand > 500:
#         cash_in_hand -= 100
#         calculate_total = cash_in_bank + cash_in_hand
#     return cash_in_hand 
# import class_11

# print(class_11.calculate_balance(10000,850))

# Class 10: (Debugging, Error handling in Python, Working with Try, Except, Else and Finally in Python)
"""Try"""
try:
    # print(g)
except:
    print("An exception occurred!")

"""Many Exceptions"""
try:
#   print(t)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

"""Else"""
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

"""Finally"""
try:
#   print(u)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

"""Raise an exception"""
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
