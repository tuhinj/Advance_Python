'''
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​the square that has side B.
e) the area of the rectangle that has sides A and B.

Input
The input file contains three double values with one digit after the decimal point.

Output
The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always with a corresponding message (in Portuguese) and one space between the two points and the value. The value calculated must be presented with 3 digits after the decimal point.
'''
values = input().split(" ")

A, B, C = values

triangle_area = (1/2)*(float(A)*float(C))
circle_area = 3.14159 * float(C)**2
trapezium_area = (1/2)*float(C)*(float(A) + float(B))
square_area = float(B)**2
rectangle_area = float(A) * float(B)

print("TRIANGULO: %.3f" %triangle_area)
print("CIRCULO: %.3f" %circle_area)
print("TRAPEZIO: %.3f" %trapezium_area)
print("QUADRADO: %.3f" %square_area)
print("RETANGULO: %.3f" %rectangle_area)