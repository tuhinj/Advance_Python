
# students = {"name": "Sohan", "age": 35, "gender": "Male"}

# print(students["age"])

# print(students.get("name"))

# students["cgpa"] = 3.58

# # students["age"] = 36
# students["age"] += 2

# print(students)

# students.update({"skill": "prgramming", "address": "Rupatoli"})

# print(students)

# # students.pop("cgpa")

# students.popitem()

# print(students)

# print(students.setdefault("weight", 56))

# # students.clear()

# # print(students)

# a = ("rahim", "karim", "sofiq")
# b = 1000

# boys = dict.fromkeys(a, b)

# print(boys)


# for key in students.keys():
#     print(key, " => ", students[key])

# for value in students.values():
#     print(value)

# for item in students.items():
#     print(item[0] , " => ", item[1])

# for key, value in students.items():
#     print(key, " => ", value)

# print(students.items())

# # name, age, weight = ("rahim", 34, 99)

# # print(name)

# # name, *others = ("rahim", 34, 99)

# # print(others)








# student = {"rahim", "karim", "rafiq"} # set

# student = {"name": "Rahim", "age": 12, "gender": "Male"}

# print(type(student))

# print(student["age"])

# student["age"] += 2

# student["cgpa"] = 3.8

# student.update({"height": 5.8, "weight": 20})

# student.pop("gender")

# student.popitem()

# # student.clear()

# # del student

# print(student.keys())

# print(student.values())

# print(student.items())

# for key in student.keys():
#     print(key)

# for value in student.values():
#     print(value)

# numbers = (1, 2, 3)
# num1, num2, num3 = (1, 2, 3)

# num1, *nums = (1, 2, 3)

# *nums, num3 = (1, 2, 3)

# print(num3)

# for item in student.items():
#     print(item)

# for key, value in student.items():
#     print(f"{key} => {value}")



# students = {"rafiq", "sofiq", "sohan", "rafiq", "salam", "sohan"}

# print(students)

# print("sofiq" in students)

# students.add("razzaq")

# students.update(["rakib", "monir", "sohan", "rahat"])

# students.remove("sohan")

# print(students)



nums1 = {1, 2, 4, 6, 9, 8}
nums2 = {4, 2, 7, 10}

# print(nums1.union(nums2))

# nums1.update(nums2)

# print(nums1)

# print(nums1.intersection(nums2))

# nums1.intersection_update(nums2)

# print(nums1)

# print(nums1.symmetric_difference(nums2))

# nums1.symmetric_difference_update(nums2)

# print(nums1)


# age = 3
# name = "Rafiq"

# print(f"{name}'s age is {age}")

# print(name + "'s age is " + str(age))




student = {"name": "Rahim", "age": 34, "gender": "Male", "asset": 5000}

print(student["age"])

student["age"] += 2

student["cgpa"] = 3.8

student.update({"height": 5.8, "weight": 45})

student.pop("age")

student.popitem()

print(student.get("boyos"))

print(student.setdefault("asset", 3000))

print(student)

# student.clear()

# print(student)

print(student.keys())

for key in student.keys():
    print(key)

print(student.values())

for value in student.values():
    print(value)

print(student.items())

# for item in student.items():
#     # print(item)
#     # print(item[0] + " => " + str(item[1]))
#     print(f"{item[0]} => {item[1]}")

# a, b = (1, 2)

# for key, value in student.items():
#     # print(item)
#     # print(item[0] + " => " + str(item[1]))
#     print(f"{key} => {value}")



students = {"rafiq", "sofiq", "sohan", "jobbar", "sohan", "rafiq"}

print(students)

# print("jovan" in students)

students.add("jovan")

students.add("jovan")

students.update(["sohid", "shakil"])

students.remove("sohan")

# students.clear()

print(students)




# nums1 = {1, 2, 4, 6, 9, 8}
# nums2 = {4, 2, 7, 10}

# print(nums1.union(nums2))

# print(nums1)

# nums1.update(nums2)

# print(nums1)

# print(nums1.intersection(nums2))

# print(nums1)

# nums1.intersection_update(nums2)

# print(nums1)

# print(nums1.symmetric_difference(nums2))

# nums1.symmetric_difference_update(nums2)

# print(nums1)



nums1 = {1,2, 3, 4, 5,6, 7, 8, 9}
nums2 = {4, 6, 9}

print(nums2.issubset(nums1))

print(nums2.issuperset(nums1))

print(nums1.issuperset(nums2))

