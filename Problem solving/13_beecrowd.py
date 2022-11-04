'''
Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:

13_beecrowd.png

Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.
'''
values = input().split(" ")
a, b, c = values

ab = (float(a) + float(b) + float(abs)(float(a)-float(b)))/2
abc = (float(b) + float(c) + float(abs)(float(ab)-float(c)))/2

print(abc,"eh o maior")

