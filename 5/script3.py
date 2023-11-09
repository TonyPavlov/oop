class Auto:
    def  __init__(self, marka, model, type, rikvypusku):
        self.marka = marka
        self.model = model
        self.type = type
        self.rikvypusku = rikvypusku
        pass

    def __str__(self):
        return f"Auto: {self.marka}, model: {self.model}, type: {self.type}, rik vypusku: {self.rikvypusku}"
        pass

auto = Auto('BMW','6 Series GT', 'Lechkovi', 2023)
print(auto)

print("--------------------------------------------")

auto.__str__()
print(auto.model)

print("---------------------------------------------")

class A(Auto):
    def __init__(self, marka, model, type, rikvypusku, cina):
        super().__init__(marka, model, type, rikvypusku, cina)
        print('Volkswagen', 'Arteon', 'lechkovi', 2022, '50000$')