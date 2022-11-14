import math
import datetime
import random

def print_student_name(student_name):
    print(f"Student name is {student_name}")

def print_student_name_with_class(student_name, class_name):
    print(f"{student_name} reads in class {class_name}")

value_of_pi = math.pi

def make_ceil(value):
    return math.ceil(value)

def return_current_date():
    return datetime.datetime.now()

def return_random_choice(names):
    return random.choice(names)