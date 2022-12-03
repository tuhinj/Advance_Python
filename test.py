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

# print# print("Hello world from ugv".startswith("ugv"))
# print("Hello world from ugv".endswith("ugv"))
# c = "!!..aw Hello world from ugv"
# #c = c.replace("world", "barishal").lstrip("!.aw ").title()
# print(c.lstrip("!.aw "))
# a = "Hello world from ugv"
# print(a[1], c[2], c[3], sep="")
# print(a[-8:-4])

# d = "Hello_world_from_ugv"
# d = d.split("_")
# d = "-".join(d)
# print(d)
# # print(" ".join(d))
# i = "Hello world"
# print(i.swapcase())
# j= "5635423465"
# print(j.isalnum())
# a = [1, 2, 3, 4, 5, 6]

# a.append(7)

# print(a)

# # a.pop()

# # print(a)
# b = [1, 2, 5, 3, 4, 5, 6, 5]
# b.remove(5)
# print(b)
# students = ["Abir", "Sohel", "Sajib", "Raihan", "Rubel"]
# a = 0
# # print(len(students))
# while a < len(students):
#     print(students[a])
#     a += 1

# def palindrome(number):
    
#     rev_num = ""
#     for num in number :
#         rev_num = num + rev_num
#     return number  == rev_num
#     return "successfully printed"

# number = input("Enter a Value : ")
# print (palindrome(number))


# def sort_words_alphabetically(sentence):

#     words = sentence.split(" ")

#     words.sort()

#     for word in words:
#         print(word)


# sort_words_alphabetically("i am not frightened of anything")

# def number_checker(number):
#     if number % 2 == 0:
#         print(number,"is even number")
#     else:
#         print(number,"is odd number")
#     return "you did it"
    
# print (number_checker(number = int(input("Enter a Value : "))))

# def number_checker(number):
#     if number > 0:
#         print("Number given by you is positive")
#     elif number < 0:
#         print("Number given by you is negative")
#     else:
#         print("Number given by you is zero")
#         return "Successfull"

# print (number_checker(number = int(input("Enter a Value : "))))
# student = {"name": "Rahim", "age": 34, "gender": "Male", "asset": 5000}
# for item in student.items():
#     print(item)
#     print(item[0] + " => " + str(item[1]))
#     print(f"{item[0]} => {item[1]}")
# for key, value in student.items():
#     print(item)
#     print(item[0] + " => " + str(item[1]))
# print(f"{key} => {value}")

# nums1 = {1,2, 3, 4, 5,6, 7, 8, 9}
# nums2 = {4, 6, 9}

# print(nums2.issubset(nums1))

# print(nums2.issuperset(nums1))
# students1 = {"shaon", "sufian", "sohrab", "risat",
#              "sohrab", "shaon", "sohan", "romiz", }
# students2 = {"kobir", "shaon", "rakib"}

# students1.discard("raihan")
# print(students1)
# if "raihan" in students1:
#     students1.remove("raihan")
# try:
#     students1.remove("raihan")
# except:
#     print("no raihan in students")
# students1.update(students2)
# print("6) :",students1)

h = ["hello", "Abdul", "zohir", "akram"]
# h.sort(reverse=True)
# h.sort()
# h.reverse()
# print(h)

# print(len({"a": 3, "b": 5}))
# print(len("hello"))
# i = h #h = ["hello", "Abdul", "zohir", "akram"]

# i = h.copy()

# i[1] = "Rahim"

# print(i)
# print(h)
















(result)

try:
    lis = [23, 29, 0, 5]
    result = lis[1]/lis[2]

    print(result)
except ZeroDivisionError:
    print("It's not possible")
finally:
    print("Done!")

print("Hello world!")