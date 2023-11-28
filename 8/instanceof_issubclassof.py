class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))  # Output: True, собака є екземпляром класу Собака
print(isinstance(dog, Animal),"\n")  # Output: True, собака є екземпляром класу Тварина (батьківського класу)



print(issubclass(Dog, Animal))  # True, Собака є підкласом класу Тварина
print(issubclass(Animal, object))  # True, Тварина є підкласом класу object (базовий клас у Python)