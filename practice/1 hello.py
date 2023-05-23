''' 1. Write a python program that takes two numbers as input and prints their sum'''
# n1 = int(input("Enter any number: "))
# n2 = int(input("Enter any number: "))

# sum = n1 + n2

# print(sum)

''' 2. Write a python program that takes a list of integer as input and pirint the sum all of even numbers in the list'''

# n_list = input("Enter some number of integer (must be comma separater): ")

# n_list = n_list.split(",")

# n_list = [int(num) for num in n_list]

# even_sum = sum(num for num in n_list if num % 2 == 0 )

# odd_sum = sum(num for num in n_list if num % 2 != 0)

# print(even_sum, odd_sum)

''' 3. Write a python program to check if a given string is a palindrome A Palindrome is a word, phrash, number, or other sequence of characters that reatds the same forward and backward'''

# def check_palindrome(words):
#     reversed_word = ""
#     for char in words:
#         reversed_word = char + reversed_word
#     return words == reversed_word

# words = input("Enter a word: ")
# print(f"{words} is Palindrome: {check_palindrome(words)}")

def check_palindrome(strings):
    reversed_word = ""
    for chr in strings:
        reversed_word = chr + reversed_word
        print(reversed_word)
    return strings == reversed_word

word = input("Enter any word: ")
print(f"{check_palindrome(word)}")

''' 4. Write a python program that reads a tesxt file and counts the frequency of each word in the file. Display the top three most frequent words along with their frequencies'''

from collections import Counter

# Read the text file
file_name = input("Enter the name of the text file: ")
with open(file_name, 'r') as file:
    text = file.read()

# Remove punctuation marks and convert to lowercase
text = text.lower()
text = ''.join(c for c in text if c.isalpha() or c.isspace())

# Split the text into words
words = text.split()

# Count the frequency of each word
word_counts = Counter(words)

# Get the top three most frequent words
top_three = word_counts.most_common(3)

# Display the top three most frequent words and their frequencies
print("Top Three Most Frequent Words:")
for word, count in top_three:
    print(f"{word}: {count}")