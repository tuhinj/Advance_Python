# introduction to string
    # a = ["hello", "hi", 1]
    # a[1] = "bye"
    # print(a)
    # b = ("hello", "hi", 3, 4)
    # print(b)
    # c = "Hello world from ugv"

# string slicing
# c = "Hello world from ugv"
# print(c[1], c[2], c[3], sep="")
# print(c[-8:-4])
# print(c[:5])
# print(c[17:])
# print(c[:-14])
# print(c[-3:])

# string modification
# upper(), lower(), strip(), replace(), split(), capitalize()
# c = "hello world from ugv. I'm Joy"
# print(c.upper())
# print(c.capitalize())
# print(c.lower())
# print(c.title())
# d = c.split()
# print(d)

# c = c.upper()
# c = c.title()
# c = c.replace("world", "barishal").lstrip().title()
# d = "Hello-world-from-ugv"
# d = c.strip("-")
# print(d)
# print(" ".join(c))

# string concatenation
# e = "Hello"
# f = "world"
# g = e + " " + f
# print(e + " " + f)
# formatting string
# print("{1} {0} from ugv".format(e, f))
# print("{b} {a} from ugv".format(a = "Hello", b = "world"))
# print(f"{e} {f} from ugv")
# string methods
# capitalize()
# startswith()
# print("Hello world from ugv".startswith("ugv"))
# endswith()
# find()
# h = "Hello woarld world"
# print(h.find("world"))
# replace()
# isalnum()
# islower()
# isupper()
# split()
# join()
# strip()
# lstrip()
# rstrip()
# upper()
# lower()
# swapcase()
i = "hello world"
print(i.swapcase())