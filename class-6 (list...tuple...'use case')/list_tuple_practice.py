'''
append() => Adds an element at the end of the list
clear()	=> Removes all the elements from the list
copy()	=> Returns a copy of the list
count()	=> Returns the number of elements with the specified value
extend() => Add the elements of a list (or any iterable), to the end of the current list
index()	=> Returns the index of the first element with the specified value
insert() => Adds an element at the specified position
pop() => Removes the element at the specified position
remove() => Removes the item with the specified value
reverse() => Reverses the order of the list
sort()	=> Sorts the list
'''

a = [1, 2, 3, 4, 5, 4, 3, 5]

a.reverse()
print(a)

# a[4] = 6

a.append(6) # 'append()' list er sese data add kora
print(len(a),"\n",a)

a.pop(2) # 'pop()' list er seser data musefele
print(len(a),"\n",a)

a.remove(5) # 'remove()' list er vitore jekono value dore dore remove kora somvob
print(len(a),"\n",a)

b = [8, 2, 3]
c = [3, 4, 5]

f = c + b # 'concat' add two list in on variable...
b.extend(c) # 'exgend()' add two variabel list 
print(f)
print(b)

b.sort() # 'sort()' list arrange cquencely...
print(b)

a.clear()

print(a)

