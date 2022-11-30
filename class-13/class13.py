# class Student:
#     def __init__(self, name, age, cgpa, roll):
#         self.name = name
#         self.age = age
#         self.cgpa = cgpa
#         self.roll = roll
#         self._pocket_money = 5000

#     def print_my_name(self):
#         print(f"My name is {self.name}")

#     def increment_my_age(self, age_to_be_incremented):
#         self.age = self.age + age_to_be_incremented

#     # private string variable_name = "dfdsfsd"

#     def purchase_something(self, amount):
#         self._pocket_money = self._pocket_money - amount
#         return self._pocket_money


#     def check_pocket_money(self):
#         return self._pocket_money


#     def __del__(self):
#         print("destructor called")

# student1 = Student("Sazzat", 25, 3.7, 13)

# print(student1.name)
# print(student1.age)
# print(student1.purchase_something(200))

# print(student1.purchase_something(500))

# student1.print_my_name()

# student1.increment_my_age(2)

# print(student1.check_pocket_money())


class Student:
    def __init__(self, name, age, cgpa, roll): # constructor
        # print(name, age, cgpa, roll, sep=" ")
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.roll = roll
        self._hand_cash = 5000
        # print("Hello from the object")

    # def increment_age(self):
    #     self.age = self.age + 1

    def increment_age(self, age_to_be_increment):
        self.age = self.age + age_to_be_increment

    # private hand_cash = 5000

    def purchase_something(self, amount):
        self._hand_cash = self._hand_cash - amount
        return f"Now you've only {self._hand_cash} taka"

    def __del__(self):
        print("Desctructor called")


student1 = Student("Antareep", 25, 3.8, 15)
student2 = Student("Sadia", 45, 4, 1201147)
print(student1)
print(student1.name)
print(student1.age)
student1.increment_age(40)
print(student1.age)
print(student1.purchase_something(300))
# print(student1._hand_cash) # don't do this