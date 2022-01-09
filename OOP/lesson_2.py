#ООП: Атрибуты и функции класса

#Класс создает свое пространство имен - это специальный словарь в котором 
# в виде ключ-значение хранятся имена переменных и функции с их значениями

class Person:
    name = "Алексей"


print(Person.__dict__) #ReadOnly словарь

#Person.__dict__['name'] = 'adaddasd' #TypeError: 'mappingproxy' object does not support item assignment

print(getattr(Person, 'name'))

setattr(Person, 'age', '24')
print(Person.__dict__) #ReadOnly словарь
delattr(Person, 'age')
print(Person.__dict__) #ReadOnly словарь
