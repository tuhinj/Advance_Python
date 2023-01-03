# Class 4: (conditional logic: if, else and elif, comparison operator and logical, operator in details, Nesting conditions, Short hand if - else (ternary))
'''Python divides the operators in the following groups:
> Arithmetic operators (+,-,*,/,%,**,//)
> Assignment operators (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)
> Comparison operators (==, !=, >, <, >=, <=)
> Logical operators (and, or, not)
> Identity operators (is, is not)
> Membership operators (in, not in)
> Bitwise operators (&: AND, |: OR, ^: XOR, ~: NOT, <<: Zero fill left shift, >>: Signed right shift)
'''
a = 12
b = 5
print(a+b,a-b,a*b,a/b,a%b,a**b,a//b)
a+=b
print(a)
a%=b
print(a)
a**=b
print(a)
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)
print(a==b and b==a)
print(a!=b or b!=a)
print(a is 23, b is not 6)
l = [1, 3, 4, 6, 9]
print(5 in l, 10 not in l)

'''conditional logic: if, else and elif'''
x = 4
y = 43
if x != y:
    print("It's correct!")

if x == y:
    print("It's Correct!")
elif x > y:
    print("It's Correct!")
else:
    print("It's not Correct!")

    '''Short Hand If'''
if x == y: print("It's correct!")
print("It's Correct!")if x > y else print("It's not Correct!")

'''Nested If'''
if x < 6 and y < 5:
    print("Condition True")
    if x != y:
        print("Condition True!")
    else:
        print("Condition False")
else:
    print("...!!!!It's Wrong!!!!...")

