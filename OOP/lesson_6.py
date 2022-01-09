# 6. ООП: Статические методы и @staticmethod

class Person:
    def hello(self):
        print('Hello')

    @staticmethod 
    #Без него выскакивает ошибка
    #TypeError: goodbye() takes 0 positional arguments but 1 was given
    def goodbye():
        print('Goodbye')

p = Person()
p.goodbye()

# Статические методы полезны когда, не требуется доступа к эземпляру класса(к его данным)
# Экономят память и ресурсы процессара 
# Может быть полезно, когда нужно объединить несколько функций в один оюъект
# многие выносят их за предел класса и описывают в глобальной области, но иногда 
# нужны лишь для данного класса.
# Ст-кие методы не связываются ни с классом, ни с его экземпляром 

a = Person()
b = Person()

print(id(a.goodbye), id(b.goodbye)) # 2967752119056 2967752119056 они равны!
print(type(a.goodbye), type(b.hello)) # <class 'function'> <class 'method'>