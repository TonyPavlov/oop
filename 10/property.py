class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радіус повинен бути більше за 0")
        else:
            self._radius  = value
    
    @property
    def diameter(self):
        return self._radius * 2
    
    @property
    def area(self):
        return 3.14 * (self._radius ** 2)
    
circle = Circle(5)

# Використання методу radius через декаратор @property
print(circle.radius)

# Використання методу setter, використовуючи декаратор @property
circle.radius = 7
print(circle.radius)

try:
    circle.radius = -2 # викличе ValueError
except ValueError as e:
    print(e)


print(circle.diameter)
print(circle.area)