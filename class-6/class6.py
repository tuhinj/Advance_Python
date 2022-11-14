a = [1, 2, 3, 4, 5, 6]

a.append(7)

print(a)

a.pop()

print(a)

a.pop(2)

print(a)

b = [1, 2, 5, 3, 4, 5, 6, 5]

c = ["hello", "world", "ugv"]

c.remove("world")

print(c)

b.remove(5)

print(b)

d = [1, 2, 3]

e = [4, 5, 6]

f = d + e # concatenation

print(d)
print(e)

# print("F is now: ",f)

# d.extend(e)

# print("d is now: ",d)

g = [3, 8, 7, 2, 9]

g.sort()

print(g)

h = ["hello", "Abdul", "zohir", "akram"]

# h.sort(reverse=True)

h.reverse()

# print(len({"a": 3, "b": 5}))
# print(len("hello"))

# h.clear()

# i = h

# i = h.copy()

# i[1] = "Rahim"

# print(i)
# print(h)

# j = (1, 2, 3, 4)
# k = (9, 8, 6)

# l = j + k

# print(l)

# def get_students():
#     # doing lots of operation
#     return ("Rahim", "Karim", "Abdul")

# student1, *otherStudents = get_students()
# # student1, student2, student3 = (1, 2, 3)

# print(otherStudents)

# m = ("Rahim", "Jakaria", "Siam", "Jakaria")


# print(m.index("Siam"))

# print(m.count("Jakaria"))

# names = ["arif", "saikat", "rabbi", "masud"]

# for index, name in enumerate(names):
#     # print(name.capitalize(), " ", index)
#     names[index] = name.capitalize()

# print(names)

# # names = [name + " - eve" for name in names]

# for name in names:
#     print(name)

names = ["arif", "saikat", "rabbi", "masud"]

# names = [name.upper() for name in names if "rabbi" == name]

names = [name.upper() if name == "rabbi" else name for name in names]

print("NAMES: ", names)

