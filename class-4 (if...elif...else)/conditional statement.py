"""Conditional Statement: if, else, elif """

student1_name = 'Joy - eve'
student2_name = 'Tuhin '

# if student1_name.endswith('eve'):
if student2_name.endswith('reg'): #truthy value "hello", 2(positive number), -3(negtive number)" #Falsy value: 0, None, False
    # student2_name = student2_name.replace('reg', 'eve')
    '''Nested condition'''
    print("Student from regular batch")
    print(student2_name)
    # if student2_name.startswith("Tuhin"):
    if student2_name.startswith("Joy"):
        print("hello Tuhin")
    else: 
        print("sorry Tuhin")
elif student2_name.endswith('eve'):
    print("Student from evening batch")

else:
    print("Sorry! you are name isn't here, pleace contect your department")

# print(student2_name)

'''Ternnery Oprator'''
print("Student from regular batch") if student2_name.endswith("reg") else print("Student from evening batch") if student2_name.endswith("eve") else print("Sorry!")
