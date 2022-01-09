#class C:
    #def __init__(self, x):
    #    self.x = x

    #@property
    #def x(self):
   #     """I'm the 'x' property."""
   #     return self._x

  #  @x.setter
  #  def x(self, value):
  #      self._x = value

  #  @x.deleter
  #  def x(self):
  #      del self._x
# 11. ООП: Свойства @property, геттеры и сеттеры (getter, setter)

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value    
