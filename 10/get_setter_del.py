class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self._price = new_price

    @price.deleter
    def price(self):
        del self._price
        print("Ціна видалена")


product = Product("Журнал", 20)

# використання getter
print(product.price)

# використання setter
product.price = 25
print(product.price)

try:
    product.price = -5
except ValueError as e:
    print(e)

# Використання deleter 
del product.price