class Parent:
     def __init__(self, x=0):
           self.__x = x

     def __str__(self):
           return str(self.__x)

class Child(Parent):
     def __init__(self, y=1):
          super().__init__()
          self.__y = y

     def __str__(self):
          return super().__str__() +","+ str(self.__y)

p = Parent()
c = Child()
print(p, c)