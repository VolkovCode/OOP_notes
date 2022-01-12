# 14. ООП: Множественное наследование, mro, миксины

class FoodMixin: # Миксин добавляет метод не связанными друг другу классам
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError("Food should be set")
        print(f"I like {self.food}")


class Person:
    
    def hello(self):
        print("I am Person")


class Student(FoodMixin, Person):
    food = "Pizza"

    def hello(self):
        print("I am student")


class Prof(Person):
    
    def hello(self):
        print("I am Prof") 


class Someone(Student, Prof):
    pass


s = Someone()

s.hello() # I am student, mro - method resolution order - кто левеее тот и прав
          
print(s.__class__.mro()) # [<class '__main__.Someone'>, <class '__main__.Student'>, <class '__main__.Prof'>, <class '__main__.Person'>, <class 'object'>]

