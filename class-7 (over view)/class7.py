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
