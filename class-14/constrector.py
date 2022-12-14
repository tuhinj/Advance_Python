
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
    
    # def __init__(self,name, age, color):
    #     self.name = name
    #     self.age = age
    #     self.color = color
    def __init__(self, name, age, color, is_active):
    #     self.name = name
    #     self.age = age
    #     self.color = color
    #     self.is_active = is_active
        super().__init__(name, age, color)
        self.is_active = is_active

class cat(Animal):
    # def __init__(self,name, age, color):
    #     self.name = name
    #     self.age = age
    #     self.color = color
    def eat_fish(self):
        return f"{self.name} Eat Fish!"
    def __str__(self):
        return f"{self.name} is {self.age} years old, it's colour {self.color}"

class cow(Animal):
    pass
    # def __init__(self,name, age, color):
    #     self.name = name
    #     self.age = age
    #     self.color = color

animal = Dog("Rokky", 1, "Black", True)
print(animal.name, animal.age, animal.color, animal.is_active,"and", animal.walk())

animal_cat = cat("Pussi", 3.5, "White")
print(animal_cat.name, animal_cat.age, animal_cat.color, "and", animal_cat.walk())

animal_cow = cow("Lalu", 4, "red")
print("Animal Name:",animal_cow.name,"\nAnimal Color:", animal_cow.color, "\nAnimal Age:", animal_cow.age)