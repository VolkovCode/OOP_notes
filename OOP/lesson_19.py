# 19. ООП: Дескрипторы данных

from time import time


#class Epoch:
    #def __get__(self, instance, owner_class):
        
        
        #print(f'Self: {self}')
        #print(f'Instance: {instance}')
        #print(f'Owner class: {owner_class}')
        #return int(time())

#class MyTime:
    #epoch = Epoch()

#m = MyTime()
#print(m.epoch) #Self: <__main__.Epoch object at 0x00000259C9DA3DC0>
               #Instance: <__main__.MyTime object at 0x00000259C9DA3D60>
               #Owner class: <class '__main__.MyTime'>
               #1642157255
               

#class Epoch:
    #def __get__(self, instance, owner_class):
    #     print(f'id of self: {id(self)}')
    #     if instance is None:
    #         return self
    #     return int(time())

    # def __set__(self, instance, value):
    #     pass


#class MyTime:
    # epoch = Epoch()

#m = MyTime()
#m1 = MyTime()


#print(m.epoch)  #id of self: 2377483042240
                #1642157806

#print(m1.epoch) #id of self: 2377483042240
                #1642157806

class IntDescriptor:
    def __init__(self):
        self._values = {}

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)

class Vector:
    x = IntDescriptor()
    y = IntDescriptor()

v = Vector()        

