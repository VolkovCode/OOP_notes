# 16. ООП: Хэшируемые объекты и равенство

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, person_obj):
        return isinstance(person_obj, Person)
        person_obj.name

p1 = Person('Алексей')
p2 = Person('Алексей')

print(p1 == p2)

            