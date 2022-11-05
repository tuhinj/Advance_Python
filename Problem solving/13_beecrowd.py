'''
Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:

13_beecrowd.png

Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.
'''
values = int(input()).split(" ")
a, b, c = values

max_num = max(values)

print(values,"eh o maior")

