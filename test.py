n = int(input())
if (n % 2 == 0 and 1 < n >=5):
    print(n + ":","Not Weird")
elif (n % 2 != 0 and 5 <= n >=20):
    print("Weird")
else:
    print(n + ":","Not Weird")