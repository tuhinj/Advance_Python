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

