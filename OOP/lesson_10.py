# 10. ООП: Область видимости классов и Методы класса @classmethod

# Пространство имен - словарь, в котором хранятся имена и их значения.
# Области видимости - путь по которому Python ищет определение имени в пространстве имен 

# local      ||
# enclosed   ||  
# Global     ||
# builtins   \/

name = 'Вова'

class Person:
    name = 'Алексей'

    def print_name(self):
        print(name)

p = Person()
p.print_name() # Вова


x = 1

def a():
    x += 1
    print()

a() #UnboundLocalError: local variable 'x' referenced before assignment 


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()
        return cls(name=name)

    @classmethod
    def from_obj(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name=name)
        return cls    
