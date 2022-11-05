a = [1, 2, 3, 4, 5, 4, 3, 5]

# a[4] = 6

a.append(6) # 'append()' list er sese data add kora
print(len(a),"\n",a)

a.pop(2) # 'pop()' list er seser data musefele
print(len(a),"\n",a)

a.remove(5) # 'remove()' list er vitore jekono value dore dore remove kora somvob
print(len(a),"\n",a)

b = [1, 2, 3]
c = [3, 4, 5]

f = b + c # 'concat' add two list in on variable...
b.extend(f) # 'exgend()' add two variabel list 
print(f)
print(b)

b.sort() # 'sort()' list arrange cquencely...
print(b)
