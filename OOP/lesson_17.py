# 17. ООП: super() и делегирование родителям

#class Person:
 #   def __init__(self, name):
 #       self.name = name

#class Student(Person):
 #   def __init__(self, name, surname):
  #      super().__init__(name)
   #     self.surname = surname


class Person:
    def hello(self):
        print(f'Bound with {self}')

class Student(Person):
    def hello(self):
        print('Student obj.hello()')
        super().hello()


s = Student()                