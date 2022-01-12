# 15. ООП: Полиморфизм, перегрузка операторов
# Полиморфизм - разное поведение одного и 
# того же метода для разных классов 

class Person:
    age = 1

    def __add__(self, value):
        self.age += 1
        return self.age

p = Person()

p + 123 # 2
p + "asdaad" # 3


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj):
        if isinstance(room_obj, Room): 
            return self.area + room_obj.area
        raise TypeError("Wrong object")

    def __eq__(self, room_obj):
        return self.area == room_obj.area

        
 # isinstance - Возвращает флаг, указывающий на то, является ли указанный объект 
 # экземпляром указанного класса (классов). Возвращает True , если указанный объект является 
 # экземпляром указанного класса (классов), либо наследующегося от него класса.

r1 = Room(3, 5)
r2 = Room(4, 7)

