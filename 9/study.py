class Figure:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def get_param(self):
        if not self.b:
            return self.a*4
        param = 2*self.a + 2*self.b
        return param
    
    def get_square(self):
        if not self.b:
            return self.a*self.a
        return self.a * self.b
    
#class Quadrate(Figure):
 #   def __init__(self, a):
  #      self.a = a

   # def get_param(self):
    #    return self.a * 4
    
    # def get_square(self):
     #   return self.a * self.a

obj_a = Figure(23, 25)
obj_b = Quadrate(14)
figure_list = [obj_a, obj_b]

for figure in figure_list:
