# 21. ООП: Метод __set_name__ и хранение данных в экземпляре класса-владельца

class ValidString:
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        print('__set__() was called')
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a String, but {type(value)} was passed')    
        key = "_" + self.property_name
        setattr(instance, key, value)

    def __get__(self, instance, owner):
        print('__set__() was called')
        if instance is None:
            return self
        #key = "_" + self.property_name
        return instance.__dict__.get(self.property_name, None)

class Person:
    name = ValidString()
    surname = ValidString()

p = Person()

# p.name = "Алексей"
# print(p.name) #Все ок
# p.name = 123
# print(p.name) #ValueError: name must be a String, but <class 'int'> was passed