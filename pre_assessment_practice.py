#1) If a word remains the same after reversing it then it's a palindrome. Now define a function to detect if a word is palindrome or not

def palindrome(word):
    revarced_word = ""
    for chr in word:
        revarced_word = chr + revarced_word
        # print(revarced_word)
    return word == revarced_word
print(palindrome("Roshe"))

"""Easy Way"""
# def palindrome(word):
#     print(word == word[::-1])
# palindrome("eye")

# 2) 1 kilometer is equal to 0.621371 mile. Now create function that can convert kilometers to mile

def input_mile(mile):
    if (type(mile) not in [int,float]):
        raise TypeError("Please Entre number not String or something")
    return mile * 0.621371
print(input_mile(12))



# 3) Write a function that can remove punctuation marks from a string
    # punctuations = "!()-[]{};:'"\,<>./?@#$%^&*_~"

def remove_punctuation(word):
    punctuations = "!()-[]{};:'\,<>.=/?@#$%^&*_~"
    renew = ""

    for chr in word:
        if chr not in punctuations:
            renew += chr
    return renew
print(remove_punctuation("J.]O/=Y"))



# 4) The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. Now write a program to print fibonacci series up to a certain number

def fibonacci_series(series_renge):
    # a, b = 0, 1
    a = 0
    b = 1
    count_exicute = 0
    while count_exicute < series_renge:
        a, b = b, a + b
        print(b)
        count_exicute+=1

fibonacci_series(10)


# 5) Write a function that can take a sentence and print each word of that sentece in alphabetic order

def sort_sentence(words):
    seprate = words.split()
    seprate.sort()
    for word in seprate:
        print(word)
sort_sentence("b c a r t w b")

# '''Easy'''
# a = input("Write a sentence: ").split(" ")
# a.sort()
# for word in a:
#     print(word)

# 6) Write a function to find even or odd

def check_EvenOdd(num):
    if num % 2 == 0:
        print(f"\"{num}\" it's an Even Number")
    else:
        print(f"\"{num}\" it's an Odd Number")
check_EvenOdd(100)


# 7) Write a program to check if a number is positive, negative or zero

def check_PosNeg(num):
    if num > 0:
        print(f"Number is Positive")
    elif num < 0:
        print(f"Number is Negtive")
    else:
        print(f"Number is Zero")
check_PosNeg(0)

# 8) If any natural number is greater than 1 and having no positive divisors other than 1 and the number itself then it's called a prime number. For example: 3, 7, 11 etc are prime numbers. Now write a function that can check if a number is prime number or not

def check_prime_number(num):
    if num > 1:
        for a in range(2, num):
            if num % a == 0:
                print("It's not a Prime Number")
                break
        else:
            print("It's a Prime Number")
    else:
        print("It's not a Prime Number")
check_prime_number(2)



# 9) Write a function to find the largest number among three given input numbers

def check_largest_number(a, b, c):
    if a > b and a > c:
        print(f"{a} is Largest then Other")
    elif b > a and b > c:
        print(f"{b} is Largest then Other")
    else:
        print(f"{c} is Largest then Other")
check_largest_number(12, 14, 16)


# A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,
    # 2017 is not a leap year
    # 1900 is a not leap year
    # 2012 is a leap year
    # 2000 is a leap year
# 10) Now write a function to check if a year is leap year or not

def check_leap_year(year):
    if year % 400 == 0:
        print(f"{year} is leap year")
    elif year % 4 == 0 and year % 100 != 0:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")
check_leap_year(1999)

# shortcut way
def check_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

check_leap_year(2000)