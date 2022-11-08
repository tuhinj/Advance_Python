nums = [2, 4, 9, 0, 1, 5, 75, 22, 42, 33]

# 1. output the length of nums list
# 2. output the list in reverse
# 3. sort the list in ascending order
# 4. sort the list in reverse order
# 5. output 4, 9, 0 from the list 
# 6. output the last element from the list
# 7. print how many even numbers in the list and how many odd numbers in the list

# 1
print("The length of nums",len(nums))

# 2
nums.reverse()
print("The reverse of list",nums)

# 3
nums.sort()
print("The reverse of list",nums)

# 4
nums.sort(reverse=True)
print("The reverse of list",nums)

# 5
print(nums[1:4])

# 6
print(nums[-1])

# 7
odd_num_count = 0
even_num_count = 0

for num in nums:
    if num % 2 == 0:
        even_num_count += 1
    else:
        odd_num_count += 1
print("Even numbers are",even_num_count,"\n"+"Odd numbers are:", odd_num_count)
