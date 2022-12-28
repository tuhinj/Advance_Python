#Leap year...
def check_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
check_leapyear(2000)
check_leapyear(2010)


# Palimdrome...
def pal(word):
    rev_w = ""
    for char in word:
        rev_w = char + rev_w
    return word == rev_w
print(pal("madam"))
print(pal("eye"))
print(pal("hello"))
