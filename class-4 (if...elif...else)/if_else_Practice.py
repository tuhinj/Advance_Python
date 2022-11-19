a = "Maynuddon - student"
b = "Tuhin - worker"
c = "Joy - teacher"

if a.endswith("student"):
    print("Dear Welcome UGV!")
elif b.startswith("Tuhin"):
    print("Sir Welcome from UGV")
else:
    print("Sorry Sir!")


'''Ternnery Oprator'''

print("Dear Welcome UGV!") if a.endswith("teacher") else print("Sorry sir!")

