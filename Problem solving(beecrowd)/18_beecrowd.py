'''  
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.

Input
The input file contains an integer value N (0 < N < 1000000).

Output
Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example. Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.
'''

a = int(input())

print(a)

b = float(a / 100)

print(" nota(s) de R$ 100,00",b)
c = float(a % 100)
print(c)
print("%.0f nota(s) de R$ 50,00"%float(c/50))
c = float(c % 50)
print("%.0f nota(s) de R$ 20,00"%float(c/20))
c = float(c % 20) 
print("%.0f nota(s) de R$ 10,00"%float(c/10))
c = float(c % 10) 
print("%.0f nota(s) de R$ 5,00"%float(c/5))
c = float(c % 5)
print("%.0f nota(s) de R$ 2,00"%float(c/2))
c = float(c % 2)
print("%.0f nota(s) de R$ 1,00"%float(c/1))
