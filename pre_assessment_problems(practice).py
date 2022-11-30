#1) If a word remains the same after reversing it then it's a palindrome. Now define a function to detect if a word is palindrome or not

def palindorme(word):
    reversed_word = ""
    for chr in word:
        reversed_word = chr + reversed_word
    return word == reversed_word
palindorme("eye") 
    

# 2) 1 kilometer is equal to 0.621371 mile. Now create function that can convert kilometers to mile

# 3) Write a function that can remove punctuation marks from a string
    # punctuations = "!()-[]{};:'"\,<>./?@#$%^&*_~"

# 4) The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. Now write a program to print fibonacci series up to a certain number

# 5) Write a function that can take a sentence and print each word of that sentece in alphabetic order

# 6) Write a function to find even or odd

# 7) Write a program to check if a number is positive, negative or zero

# 8) If any natural number is greater than 1 and having no positive divisors other than 1 and the number itself then it's called a prime number. For example: 3, 7, 11 etc are prime numbers. Now write a function that can check if a number is prime number or not

# 9) Write a function to find the largest number among three given input numbers


# A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,
    # 2017 is not a leap year
    # 1900 is a not leap year
    # 2012 is a leap year
    # 2000 is a leap year

# 10) Now write a function to check if a year is leap year or not

