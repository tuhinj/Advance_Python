'''  
Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.
'''

a = float(input())

print(a)
print("%.0f nota(s) de R$ 100.00"%int(a / 100))
c = float(a % 100)
print("%.0f nota(s) de R$ 50.00"%int(c/50))
c = float(c % 50)
print("%.0f nota(s) de R$ 20.00"%int(c/20))
c = float(c % 20) 
print("%.0f nota(s) de R$ 10.00"%int(c/10))
c = float(c % 10) 
print("%.0f nota(s) de R$ 5.00"%int(c/5))
c = float(c % 5)
print("%.0f nota(s) de R$ 2.00"%int(c/2))

print("MOEDAS:")
c = int(c % 2)
print("%.0f nota(s) de R$ 1.00"%float(c/1))

b = a * 100

c = int(b % 100)
print("%.0f nota(s) de R$ 0.50"%float(c/50))
c = int(c % 50)
print("%.0f nota(s) de R$ 0.25"%float(c/25))
c = int(c % 25)
print("%.0f nota(s) de R$ 0.10"%float(c/10))
c = int(c % 10)
print("%.0f nota(s) de R$ 0.05"%float(c/5))
c = int(c %5)
print("%.0f nota(s) de R$ 0.01"%float(c/1))