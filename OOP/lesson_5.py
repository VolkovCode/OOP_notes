# 5. ООП: Инициализация экземляров, __init__ метод

class Person:
    def create(self):
        self.name = 'Алексей'

    def display(self):
        print(self.name)

p = Person()

#p.display() # AttributeError: 'Person' object has no attribute 'name'
#Это происходит из-за того что локальный словарь __dict__ у экземпляра пустой {}

p.create() # но это неудобно
print(p.__dict__) #{'name': 'Алексей'}

class Person:
    def __init__(self, name):
        self.name = 'Алексей'

    def display(self):
        print(self.name)