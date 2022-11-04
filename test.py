# n = int(input())
# if (n % 2 == 0 and 1 < n >=5):
#     print(n + ":","Not Weird")
# elif (n % 2 != 0 and 5 <= n >=20):
#     print("Weird")
# else:
#     print(n + ":","Not Weird")

line1 = input().split(" ")
line2 = input().split(" ")
cod1, num1, price1 = line1
cod2, num2, price2 = line2
total = (int(num1) * float(price1)) + (int(num2) * float(price2))
print(f'VALOR A PAGAR: R$ {total:.2f}')        