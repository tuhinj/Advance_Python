#1) If a word remains the same after reversing it then it's a palindrome. Now define a function to detect if a word is palindrome or not

def is_palindrome(word):
    reversed_word = ""

    for char in word:
        reversed_word = char + reversed_word

    return word == reversed_word

print(is_palindrome("eye"))


# 2) 1 kilometer is equal to 0.621371 mile. Now create function that can convert kilometers to mile

def convert_to_miles(kilometers):

    if (type(kilometers) not in [float, int]):
        raise TypeError("Please enter kilometers as a number")

    return kilometers * 0.621371

print(convert_to_miles(5))


# 3) Write a function that can remove punctuation marks from a string
    # punctuations = "!()-[]{};:'"\,<>./?@#$%^&*_~"

def punctuations_remover(string):
    punctuations = "!()-[]{};:\,<>./?@#$%^&*_~"

    fresh_word = ""

    for char in string:
        if char not in punctuations:
            fresh_word += char

    return fresh_word


print(punctuations_remover("He,ll.o>"))


# 4) The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. Now write a program to print fibonacci series up to a certain number

def fibonacci_printer(end_number):
    a, b = 0, 1
    count = 0
    while count < end_number:
        a, b = b, a + b
        print(b)
        count += 1

fibonacci_printer(10)


# 5) Write a function that can take a sentence and print each word of that sentece in alphabetic order

def sort_words_alphabetically(sentence):

    words = sentence.split(" ")

    words.sort()

    for word in words:
        print(word)


sort_words_alphabetically("hi we are learning python and it's awesome")


# 6) Write a function to find even or odd

def number_checker(number):
    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")

number_checker(5)


# 7) Write a program to check if a number is positive, negative or zero

def number_checker(number):
    if number > 0:
        print("Number given by you is positive")
    elif number < 0:
        print("Number given by you is negative")
    else:
        print("Number given by you is zero")

number_checker(-9)


# 8) If any natural number is greater than 1 and having no positive divisors other than 1 and the number itself then it's called a prime number. For example: 3, 7, 11 etc are prime numbers. Now write a function that can check if a number is prime number or not

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


# 9) Write a function to find the largest number among three given input numbers

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


# A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,
    # 2017 is not a leap year
    # 1900 is a not leap year
    # 2012 is a leap year
    # 2000 is a leap year

# 10) Now write a function to check if a year is leap year or not

def check_leap_year(year):
    # century year divided by 400 is leap year
    if year % 400 == 0:
        print(f"{year} is a leap year")

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is a leap year")

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        print(f"{year} is not a leap year")


check_leap_year(2009)


# shortcut way
def check_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

check_leap_year(2009)