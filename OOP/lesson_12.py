class Human:
    """Человек, возраст которого не может быть больше 120 и меньше 0"""

    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 120 and age >= 0:
            self.__age = age
        else:
            self.__age = 0

h = Human(30)
h.age =150
print(h.age)
