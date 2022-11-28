
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def walk(self):
        return f"{self.name} is Walking"

    def sound(self):
        return f"{self.name} is Barking"

class Dog(Animal):
    pass
    # def __init__(self,name, age, color):
    #     self.name = name
    #     self.age = age
    #     self.color = color

class cat(Animal):
    pass
    # def __init__(self,name, age, color):
    #     self.name = name
    #     self.age = age
    #     self.color = color
    def eat_fish(self):
        return f"{self.name} Eat Fish!"

class cow(Animal):
    pass
    # def __init__(self,name, age, color):
    #     self.name = name
    #     self.age = age
    #     self.color = color

animal = Dog("Tom", 1, "Black")
print(animal.name, animal.age, animal.color,"and", animal.walk())

animal_cat = cat("Pussi", 3.5, "White","/n")
