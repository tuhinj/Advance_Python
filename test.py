# a = {"name":"joy", "age": 12}

# # import pdb; pdb.set_trace()

# print(a.values())

# print(a.keys())

# print(a.keys())


# num = 5 + '5'

# try:
#     num = 5 + int("5")
# except ValueError:
#     print("Something wrong")

# lis = [23, 29, 0, 5]
# result = lis[1]/lis[2]

# print(result)

try:
    lis = [23, 29, 0, 5]
    result = lis[1]/lis[2]

    print(result)
except ZeroDivisionError:
    print("It's not possible")
finally:
    print("Done!")

print("Hello world!")