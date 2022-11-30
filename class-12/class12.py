# class_name_one #snake case (used for naming variables and function)
# classNameOne #camel case
# ClassNameOne #pascal case (used for naming classes)

# class Student:
#     name = "Sohan"
#     age = 45

#     def do_math(self):
#         return 3 + 5

# student1 = Student()
# student2 = Student()

# print(student1.name)
# print(student1.age)

# print(student2.name)
# print(student2.age)

# print(student1 is student2)

# class Student:
#     def __init__(self, name, age, cgpa):
#         self.name = name
#         self.age = age
#         self.cgpa = cgpa
#         # print("Hello again")

#     def __del__(self):
#         print("Destructor called")

#     def print_my_name(self):
#         print(f"My name is {self.name}")

# student1 = Student("Akash", 25, 3.1)
# student2 = Student("Opey", 32, 1.3)

# student1.print_my_name()

# print(f"student1 name is {student1.name}. student1 age is {student1.age}. student1 cgpa is {student1.cgpa}")









# def function_name():
#     pass

# class Student:
#     def __init__(self, name, age, cgpa, roll):
#         self.name = name
#         self.age = age
#         self.cgpa = cgpa
#         self.roll = roll

#     def participate_exam(self):
#         print(f"{self.name} participated the exam")

#     def increment_birth_year(self, age_to_be_incremented):
#         self.age = self.age + age_to_be_incremented
#         # self.age += 1


# student1 = Student("Akash", 22, 3.8, 24)
# student2 = Student("Azmal Gazi", 30, 4, 32)

# print(student1.name)
# print(student1.age)
# student1.participate_exam()
# student1.increment_birth_year(10)
# print(student1.age)

# print(student2.name)
# print(student2.cgpa)
# student2.participate_exam()






# def function_name():
#     pass

# function_name()

# class Student:
#     pass

# ClassName()

class Student:
    def __init__(self, name, age, cgpa, roll):
        # print(name, age, cgpa, roll, sep=" ")
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.roll = roll
        # print("Hello from the object")

    # def increment_age(self):
    #     self.age = self.age + 1

    def increment_age(self, age_to_be_increment):
        self.age = self.age + age_to_be_increment


student1 = Student("Antareep", 25, 3.8, 15)
student2 = Student("Sadia", 45, 4, 1201147)
print(student1.name)
print(student1.age)
student1.increment_age(40)
print(student1.age)

print(student2.name)
print(student2.age)
student2.increment_age(1)
print(student2.age)

# student2 = Student()

# print(student1.name, student1.age)
# print(student2.name, student2.age)

# # print(student1 == student2)
# print(student1 is student2)