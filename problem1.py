# find who is the elder brother (print "name is the elder brother")
# Check his age even or odd

rahims_age = 55
karims_age = 93
abduls_age = 72

if rahims_age > karims_age  and rahims_age > abduls_age:
    print("Rahim is Elder Brother")
    if rahims_age % 2 == 0:
        print("It's Even")
    else:
        print("It's Odd")
elif karims_age > rahims_age and karims_age > abduls_age:
    print("Karim is elder brother")
    if karims_age % 2 == 0:
        print("It's Even")
    else:
        print("It's Odd")
else:
    print("Abdul is elder brother")
    if abduls_age % 2 == 0:
        print("It's Even")
    else:
        print("It's Odd")
    