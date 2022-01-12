# 12. ООП: Свойства только для чтения и вычисляемые свойства

class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None #Для кэшироввания

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None

    @property
    def surname(self):
        return self._surname
        

    @name.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None  #Для кэшироввания  


    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = f'{self._name} {self._surname}' #Для кэшироввания
        return self._full_name


p = Person("Алексей", "Волков")

print(p.__dict__)
print(p.full_name)
print(p.__dict__)
p.surname = "Иванов"
print(p.__dict__)
print(p.full_name)


