class Human: 
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = name + ' ' + surname
    
    def show_name(self):
        print(self.name)
    
    def _show_surname(self):
        a = self.__show_name_surname()
        print(a)
        # print(self.surname)
    
    def __show_name_surname(self):
        # print(self.name, self.surname)
        return self.full_name

    

name = Human('Anton', 'Pavlov')
Human._show_surname()

