#Перегрузка операций


# Перегрузка операций - означает перехват встроенных операций в методах класса - 
# Python автоматически вызывает ваши методы, когда экземпляры класса обнаруживаются
# во встроенных операциях, и возвращаемое значение вашего метода становится результатом
# соответствующей операциию Ниже приведен обзор ключевых идей, лежащих в основе перегрузки.

#  1) Перегрузка операций позволяет перехватывать нормальные операции Python.
#  2) Классы могут перегружать все операции выражений Python. 
#  3) Классы также могут перегружать встроенные операции, такие как вывод,
#     вызовы функций, доступ к атрибутам и т.д.
#  4) Перегрузка делает экземпляры классов более похожими на встроенные типы.
#  5) Перегрузка реализуется за счет предоставления особым образом именнованных 
#     методов в классе.   

#---------------------- Конструкторы и выражения: __init__ и __sub__ -------------------------#

# __init__  применяется для инициализации вновь созданного объекта экземпляра с
# использованием любых аргуметов, указываемых после имени класса
# Метод __sub__ исполняет роль бинарной операции аналагично методу __add__
# перехватывая выражения вычитания и возвращая в качестве своего результата новый экземпляр 
# класса (попутно выполняя __init__)

class Number:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other):
        return Number(self.data - other)

x = Number(5)
y = x - 2 
#print(y.data)  # 3   

#-------------------------------- Индексирование и нарезание: --------------------------------#
# __getitem__ и __setitem__

class Indexer:
    def __getitem__(self, index):
        return index ** 2

a = Indexer()
print(a[2]) # 4

class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

a = Indexer()
print(a[0])   
#  getitem: 0
#  5
print(a[1])
# getitem: 1
# 6
print(a[-1]) 
# getitem: -1
# 9       
print(a[2:4])
# getitem: slice(2, 4, None)
# [7, 8]

class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)    

A = Indexer()
print(A[99]) 
# indexing 99 
# None
print(A[1:99:2]) 
# slicing 1 99 2
# None
print(A[1:]) 
# slicing 1 None None
# None         

#-------------------------Итерация по индексам: __getitem__ ----------------------------------#

class StepperIndex: 
    def __getitem__(self, i): #без него 'StepperIndex' object is not subscriptable
        return self.data[i]

SI = StepperIndex()
SI.data = 'Spam'

print(SI[3])
for item in SI:
    print(item, end=' ')

#---------------------------------Членство: __contains__, __iter__, __getitem__---------------#

class  Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end='') #Запасной вариант для итерации
        return self.data[i]    # Также для индексирования, нарезания

    def __iter__(self): #Предпочтительнее для итерации
        print('iter=> ', end='') # Допускает только один активный итератор
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x): #Предпочтительнее для операции in
        print('contains: ', end='')
        return x in self.data

I = Iters([1, 2, 3, 4, 5])
print(3 in I)
for i in I:
    print(i, end=' | ') 
print()
print([i ** 2 for i in I])
print(list(map(bin, I)))       
It = iter(I)

while True:
    try:
        print(next(It), end=' @ ')
        print(I.__dict__)
        print(It.__dict__)
    except StopIteration:
        break

#----------------------Доступ к атрибутам: __getattr__ и __setattr__ -------------------------#

#Лучший способ в 39 главе

#---------------------Строковое представление: __repr__, __str__ -----------------------------#

# * Метод __str__ сначала опробуется для операции print  и встроенной функции str(внутренний 
#   эквивалент которой запускает операция print). В общем случае он должен возвратить отображение,
#   дружественное пользователю.

# * Метод __repr__ используется во всех остальных контекстах: для эхо-вывода в интерактивной подсказке
#   функции repr и вложеных появлений, а также print и str, если метод __str__ осутствует. В общем случае
#   он должен возвратить строку как в коде, которую можно было бы применить для воссоздания объекта,
#   или детальное отображение для разработчиков




      