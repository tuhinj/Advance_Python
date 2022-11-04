# n = int(input())
# if (n % 2 == 0 and 1 < n >=5):
#     print(n + ":","Not Weird")
# elif (n % 2 != 0 and 5 <= n >=20):
#     print("Weird")
# else:
#     print(n + ":","Not Weird")

linha1 = input().split(" ")
linha2 = input().split(" ")
cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2
total = (int(qtde1) * float(valor1)) +                    (int(qtde2) * float(valor2))
print(f'VALOR A PAGAR: R$ {total:.2f}')        