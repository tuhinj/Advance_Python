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
