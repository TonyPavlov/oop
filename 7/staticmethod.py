class Mathematics:

    def addNumbers(x,y):
        return x + y

#Створюємо статичний метод addNumber()
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5,34))