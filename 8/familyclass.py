class Animal:
    def __init__(self, name, age):
        self.name = name
        self.year = age

    def introduce(self):
        return f"Привіт, Я {self.name}"

# Дочірній клас, що успадковує Тварина

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def introduce(self):
        return f"Привіт, я {self.name}, кіт породи {self.breed}!"

# Ще один дочірній клас, що успадковує Тварина

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def introduce(self):
        return f"Привіт, я {self.name}, собака породи {self.breed}!"

cat = Cat("Мурка", 4, "Перс")
dog = Dog("Карл", 5, "лабрадор")

print(cat.introduce())
print(dog.introduce())