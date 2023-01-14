# Class 11: (Iterators, Generators, Decorators)
"""Iterators"""
foots = ("Apple", "Banana", "Orange", "Gohaba")
foot = iter(foots)

print(next(foot))
print(next(foot))
print(next(foot))
print(next(foot))

a = "apple"
b = iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

'''Create an Iterator'''
class mynum:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
class1 = mynum()
myiter = iter(class1)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

"""Generators"""
input('What is your name?')