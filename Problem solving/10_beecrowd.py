'''In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

Input
The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point.

Output
The output file must be a message like the following example where "Valor a pagar" means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.
'''
product_code_one = int(input())
product_number_one = int(input())
product_price_one = float(input())

product_code_two = int(input())
product_number_two = int(input())
product_price_two = float(input())

line_one = [product_code_one,product_number_one,product_price_one]
line_two = [product_code_two,product_number_two,product_price_two]

# pay = float((product_number_one*product_price_one) + (product_number_two*product_price_two))
paid = float((line_one[1]*line_one[2]) + line_two[1]*line_two[2])

print("VALOR A PAGAR: R$ %.2f"%paid)