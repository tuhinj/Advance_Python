
# #1.Write a Python function to sum all the numbers in a list
# Sample list: [8, 2, 3, 0, 7]

def add_function(lst):
    add = 0
    for num in lst:
        add = add + num
    return add

sum_list = [8, 2, 3, 0, 7]
print(f"SUM: {add_function(sum_list)}")


# 2) Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
# Sample list: “The quick Brown Fox”
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def calculate_string(line):
    upper = 0
    lower = 0

    for char in line:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1

    print(f"No. of upper case character : {upper}")
    print(f"No. of lower case character : {lower}")

strings = input("Give Your line here: ")
calculate_string(strings)

# 3) Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
# Expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

def dictionary_function():
    output_dect ={}
    for num in range(1, 16):
        output_dect[num] = num ** 2
    return output_dect

print(dictionary_function())

# 4) Write a Python program to sum all the items in a dictionary
# Sample dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

def sum_dictionary(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total

dictionary = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
print(f"Sum of Dict: {sum_dictionary(dictionary)}")


# 5) Write a Python program to create a symmetric difference set of set a and b
# a = {1, 3, 5, 9, 6}
# b = {2, 5, 7, 4, 1}
# Expected output: {3, 2, 7, 9, 6, 4}

a = {1, 3, 5, 9, 6}
b = {2, 5, 7, 4, 1}
result = a.symmetric_difference(b)
print(result)


# 6) Write a Python program to remove all elements from a given set.
# Sample input: {3, 2, 7, 9, 6, 4}
# Expected output: {}

def clear_set(my_set):
    while my_set:
        my_set.pop()

my_set = {3, 2, 7, 9, 6, 4}
clear_set(my_set)
print(my_set)

# 7) If a word remains the same after reversing it then it's a palindrome. Now define a function to detect if a word is palindrome or not

def check_palindrome(words):
    reversed_word = ""
    for char in words:
        reversed_word = char + reversed_word
    return words == reversed_word

words = input("Enter a word: ")
print(f"{words} is Palindrome: {check_palindrome(words)}")

# 8) 1 kilometer is equal to 0.621371 mile. Now create function that can convert kilometers to mile

def kilo_to_mile(kilo):
    converted = kilo * 0.612371
    return converted

value = float(input("Enter Value in Kilometer: "))
print(f"{kilo_to_mile(value)}")

# 9) Write a function that can remove punctuation marks from a string
#     # punctuations: "!()-[]{};:'"\,<>./?@#$%^&*_~"

def punctuations_remover(string):
    punctuations = "!()-[]{\};:\,<>./?@#$%^&*_~"
    fresh_word = ""

    for char in string:
        if char not in punctuations:
            fresh_word += char

    return fresh_word


print(punctuations_remover("He,ll.o>"))


# 10) The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. Now write a program to print fibonacci series up to a certain number

def fibonacci_printer(end_number):
    a, b = 0, 1
    count = 0
    while count < end_number:
        a, b = b, a + b
        print(b)
        count += 1

fibonacci_printer(10)

# 11) Write a function that can take a sentence and print each word of that sentence in alphabetic order

def sort_words_alphabetically(sentence):
    words = sentence.split(" ")
    words.sort()
    for word in words:
        print(word)


sort_words_alphabetically("hi we are learning python and it's awesome")

# 12) Write a function to find even or odd

def number_checker(number):
    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")

number_checker(5)

# 13) Write a program to check if a number is positive, negative or zero

def number_checker(number):
    if number > 0:
        print("Number given by you is positive")
    elif number < 0:
        print("Number given by you is negative")
    else:
        print("Number given by you is zero")

number_checker(-9)

# 14) If any natural number is greater than 1 and having no positive divisors other than 1 and the number itself then it's called a prime number. For example: 3, 7, 11 etc are prime numbers. Now write a function that can check if a number is prime number or not

def prime_checker(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(f"{number} is not a prime number")
                break
        else: # NOTICE THIS ELSE BLOCK IS PART OF FOR STATEMENT NOT A PART OF IF STATEMENT
            print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

prime_checker(10)

# 15) Write a function to find the largest number among three given input numbers

def find_largest_number(number1, number2, number3):
    largest = number1

    if (number1 > number2) and (number1 > number3):
        largest = number1
    elif (number2 > number1) and (number2 > number3):
        largest = number2
    else:
        largest = number3

    print(f"The largest number is {largest}")


find_largest_number(15, 23, 8)

# # A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,
#     # 2017 is not a leap year
#     # 1900 is a not leap year
#     # 2012 is a leap year
#     # 2000 is a leap year

# 16) Now write a function to check if a year is leap year or not

def check_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

check_leapyear(2009)

# 17) Program that takes a list of strings as input and prints
# the longest string from the list

def longest_string(lists):
    longest_string = ""
    for string in lists:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

inputs = ["Hello", "ugv", "fcuk"]
longest = longest_string(inputs)
print(f"Longest string: {longest}")

# 18) Read a string and print the count of each vowel in the string

def count_vowel(strings):
  vowels = "aeiouAEIOU"
  vowel_count = 0
  # show_vowels = ""

  for char in strings:
    if char in vowels:
      # show_vowels += char
      vowel_count += 1
  return vowel_count
  

inputs = "hello betichOd"

result = count_vowel(inputs)
print(result)

# 19) Write a program that takes a list of integers as input and print
# the sum of all even number

def sum_number(num):
    sum = 0
    for i in num:
        if i % 2 == 0:
            sum = sum + i
    return sum

numbers = [2, 3, 5, 6, 8, 10]
result = sum_number(numbers)
print(result)

# 20) Write a program that reads a text file and counts the frequency of each
# word in the file. Display the top three most frequent word
# along with the frequencies

