class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        return "Муррр!"
    
    def chese_mouse(self, mouse):
        return f"{self.name} ловить {mouse.name}"
    
class Mouse(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        return "Пііі!"

cat = Cat("Василь")
mouse = Mouse("Жужа")

# Використання методів об'єктів одного класу в іншому класі

print(cat.make_sound())
print(mouse.make_sound())

print(cat.chese_mouse(mouse))