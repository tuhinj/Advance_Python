#Leap year...
def check_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
check_leapyear(2000)

# Palimdrome...
def pel(w):
    rev_w = ""
    for char in w:
        rev_w = char + rev_w
    return w == rev_w
print(pel("madam"))

