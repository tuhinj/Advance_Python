# function

def print_hello():
    print("hello")

# print_hello()

def print_hello(neme):
    print(f"Hello {neme}")

print_hello("joy")

students = []
def set_winers(first_winner, second_winner, third_winner):
    global students
    students["first_winner"] = first_winner
    students["second_winner"] = second_winner
    students["third_winner"] = third_winner

set_winers("Joy", "pronoy","Rahat")
print(students)