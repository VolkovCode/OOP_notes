# 4. ООП: Функции классов и методы экземпляров, self

class Person:
    
    #@staticmethod
    def hello():
        print('Привет')

p = Person()        

print(type(p.hello), type(Person.hello))

p.hello() #TypeError: hello() takes 0 positional arguments but 1 was given

# Методы - это специальные классы-обертки, которые объединяют в себе функции 
# класса и конкретный экземпляр данного класса
