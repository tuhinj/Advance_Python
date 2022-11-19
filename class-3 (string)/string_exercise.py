a = "Hello my name is Maynuddin Tuhin Joy"

print(a[17:])

print(len(a))

print(a[:-30])

print(a.upper())

print(a.lower())

print(a.capitalize())

print(a.title())

b = "  hello world!    "

print(b)

print(b.strip())

print(b.rstrip())

print(b.lstrip())

print(b.split())

print(b.replace("world", "Bangladesh").strip().title())

print(" ".join(b).strip())

e = "HELLO"
f = "hello"

print(e.isupper(),"\n",a.isupper())

print(e.isalnum(),a.isalnum())

print(e.isalpha())

print(f.islower())

print("end:",a.endswith("Joy"))

print("start:",b.startswith("Hello"))

print(a.find("Tuhin"))




# Concatination...

print(b.strip() + a)

print(a,b.strip())

print("Hello I'm From {f}, My name is {n}". format(f = "Bangladesh", n = "Maynuddin Tuhin Joy"))

print("{0} {1} from ugv".format(b.strip().capitalize(), a))

print(f"Hi: {b.capitalize().strip()}, \nWhat is your name: {a}")