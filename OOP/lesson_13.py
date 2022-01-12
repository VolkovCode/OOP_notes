 # 13. ООП: Наследование, перегрузка методов и расширение функциональности


#class Person: #Наследование
    #def hello(self):
        #print('I am Person')


#class Student(Person):
    #def hello(self): #Перегрузка методов
        #print("I am student") 


class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello from {self.name}') 


class Student(Person):
    def goodbye(self):
        print(f"Пока {self.name}")


s = Student('Алексей')

s.goodbye()





