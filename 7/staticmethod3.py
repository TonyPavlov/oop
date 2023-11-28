class MyClass: 
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    
    @staticmethod
    def from_string(string_data):
        args = string_data.split(',')
        return MyClass(args[0], args[1])

obj = MyClass.from_string("hello, world")
print("arg1:",obj.arg1)
print("arg2:",obj.arg2)

