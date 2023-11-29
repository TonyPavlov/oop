# Поліформізм
class City:
    def __init__(self, name, population):
        self.name = self.set_name(name)
        self.population = population

    def set_name(self, name):
        if not name:
            print("please check name of city")
        name = "Name city: " + name
        return name
    
    
    def get_name(self):
        return self.name

    @classmethod
    def check_population(cls):
        

    def check_population(self):
        if self.population > 100000:
            print("big city")
        else:
            print("town")



class InfoCity(City):
    @staticmethod
    def check_population(self):
        if population > 100000:
             print("This city has mer")
             print("big city")
        else:
            print("This town has holova")
            print("town")



#obj = City("Dublyany",9000)
#obj1 = City("Lviv",800000)
#obj2 = City("Vynnyky",200000)

#cities = [obj, obj1, obj2]

#for city in cities:
#    print(city.get_name())
#    city.population